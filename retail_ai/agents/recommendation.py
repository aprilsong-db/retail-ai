"""
Recommendation Agent

This module contains the recommendation agent that handles product
recommendations and personalized suggestions.
"""

from typing import Any, Sequence

import mlflow
from databricks_langchain import ChatDatabricks
from langchain_core.language_models import LanguageModelLike
from langchain_core.messages import BaseMessage
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import create_react_agent
from loguru import logger
from mlflow.models import ModelConfig
from langchain.prompts import PromptTemplate

# Optional imports for guardrails
try:
    from retail_ai.guardrails import reflection_guardrail, with_guardrails
    GUARDRAILS_AVAILABLE = True
except ImportError:
    GUARDRAILS_AVAILABLE = False

from retail_ai.state import AgentConfig, AgentState
from retail_ai.tools import (
    create_find_product_by_sku_tool,
    create_find_inventory_by_sku_tool,
    create_find_store_inventory_by_sku_tool,
    find_product_details_by_description_tool,
    create_similar_products_recommendation_tool,
)
from retail_ai.types import AgentCallable


def recommendation_agent(model_config: ModelConfig) -> AgentCallable:
    """
    Create a recommendation agent that handles product recommendation queries.

    Args:
        model_config: Model configuration containing recommendation agent settings

    Returns:
        An agent callable function that handles recommendation queries
    """
    logger.debug("Creating recommendation agent")
    
    # Get agent configuration using the same pattern as other agents
    model: str = model_config.get("agents").get("recommendation").get("model").get("name")
    prompt: str = model_config.get("agents").get("recommendation").get("prompt")
    guardrails: Sequence[dict[str, Any]] = (
        model_config.get("agents").get("recommendation").get("guardrails") or []
    )
    
    # Get retriever configuration
    retriever_config: dict[str, Any] = model_config.get("retrievers").get("products_retriever")
    index_name: str = retriever_config.get("vector_store").get("index_name")
    endpoint_name: str = retriever_config.get("vector_store").get("endpoint_name")
    columns: Sequence[str] = retriever_config.get("columns")
    search_parameters: dict[str, Any] = retriever_config.get("search_parameters", {})
    num_results: int = search_parameters.get("num_results", 10)
    
    # Get warehouse configuration
    warehouse_id: str = (
        model_config.get("resources")
        .get("warehouses")
        .get("shared_endpoint_warehouse")
        .get("warehouse_id")
    )
    
    @mlflow.trace()
    def recommendation(state: AgentState, config: AgentConfig) -> dict[str, Any]:
        """
        Handle product recommendation queries using vector search and inventory data.
        
        This agent:
        1. Uses vector search to find similar products based on user preferences
        2. Looks up detailed product information for similar items
        3. Checks inventory availability for recommended products
        4. Provides personalized recommendations with explanations
        """
        logger.debug(f"Recommendation agent processing: {len(state.get('messages', []))} messages")
        
        try:
            # Create LLM
            llm: LanguageModelLike = ChatDatabricks(model=model, temperature=0.1)
            
            # Create prompt template
            prompt_template: PromptTemplate = PromptTemplate.from_template(prompt)
            configurable: dict[str, Any] = {
                "user_id": state["user_id"],
                "store_num": state["store_num"],
            }
            system_prompt: str = prompt_template.format(**configurable)
            
            # Create tools for recommendation agent
            tools = []
            
            # Specialized recommendation tool that combines vector search with inventory data
            if endpoint_name and index_name and columns and warehouse_id:
                similar_products_tool = create_similar_products_recommendation_tool(
                    endpoint_name=endpoint_name,
                    index_name=index_name,
                    columns=columns,
                    warehouse_id=warehouse_id,
                    model_config=model_config,
                    k=5,  # Return top 5 similar products
                )
                tools.append(similar_products_tool)
                logger.debug("Added similar products recommendation tool")
            
            # Fallback vector search tool for general product discovery
            if endpoint_name and index_name and columns:
                vector_search_tool = find_product_details_by_description_tool(
                    endpoint_name=endpoint_name,
                    index_name=index_name,
                    columns=columns,
                    k=num_results,
                )
                tools.append(vector_search_tool)
                logger.debug("Added vector search tool")
            
            # Product lookup tools
            if warehouse_id:
                product_sku_tool = create_find_product_by_sku_tool(warehouse_id, model_config)
                tools.append(product_sku_tool)
                logger.debug("Added product lookup tools")
                
                # Inventory tools
                inventory_sku_tool = create_find_inventory_by_sku_tool(warehouse_id, model_config)
                store_inventory_tool = create_find_store_inventory_by_sku_tool(warehouse_id, model_config)
                tools.extend([inventory_sku_tool, store_inventory_tool])
                logger.debug("Added inventory tools")
            
            if not tools:
                logger.warning("No tools configured for recommendation agent")
            
            # Create the agent
            agent: CompiledStateGraph = create_react_agent(
                model=llm,
                tools=tools,
                prompt=system_prompt,
            )
            
            # Apply guardrails if configured and available
            if GUARDRAILS_AVAILABLE:
                for guardrail_definition in guardrails:
                    guardrail: CompiledStateGraph = reflection_guardrail(guardrail_definition)
                    agent = with_guardrails(agent, guardrail)
            elif guardrails:
                logger.warning("Guardrails configured but guardrails module not available")
            
            # Invoke the agent with the current state
            result = agent.invoke(state, config)
            logger.debug("Recommendation agent completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Recommendation agent error: {e}")
            # Return a fallback response
            from langchain_core.messages import AIMessage
            fallback_message = AIMessage(
                content="I apologize, but I'm having trouble accessing our product recommendation system right now. "
                       "Please try asking about specific products or speak with a store associate for personalized recommendations."
            )
            return {"messages": [fallback_message]}
    
    return recommendation 