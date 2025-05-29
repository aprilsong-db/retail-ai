"""
General Agent

This module contains the general agent that handles general customer service queries,
store information, and complex analytical questions using Genie.
"""

from typing import Any, Sequence

import mlflow
from databricks_langchain import ChatDatabricks
from langchain.prompts import PromptTemplate
from langchain_core.language_models import LanguageModelLike
from langchain_core.messages import BaseMessage
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import create_react_agent
from loguru import logger
from mlflow.models import ModelConfig

from retail_ai.state import AgentConfig, AgentState
from retail_ai.types import AgentCallable
from retail_ai.tools.store import find_store_details_by_location_tool
from retail_ai.tools.genie import create_genie_query_tool
from retail_ai.tools.customer import create_customer_profile_intelligence_tool

# Optional imports for guardrails
try:
    from retail_ai.guardrails import reflection_guardrail, with_guardrails
    GUARDRAILS_AVAILABLE = True
except ImportError:
    GUARDRAILS_AVAILABLE = False


def general_agent(model_config: ModelConfig) -> AgentCallable:
    """
    Create a general agent that handles general customer service queries and Genie analytics.

    This agent specializes in store information, general customer service,
    and complex analytical questions using Databricks Genie.

    Args:
        model_config: Model configuration containing general agent settings

    Returns:
        An agent callable function that handles general queries
    """
    model: str = model_config.get("agents").get("general").get("model").get("name")
    prompt: str = model_config.get("agents").get("general").get("prompt")
    guardrails: Sequence[dict[str, Any]] = (
        model_config.get("agents").get("general").get("guardrails") or []
    )

    warehouse_id: str = (
        model_config.get("resources")
        .get("warehouses")
        .get("shared_endpoint_warehouse")
        .get("warehouse_id")
    )

    # Get vector search configuration for stores
    stores_vector_store = model_config.get("resources").get("vector_stores").get("store_vector_store")
    store_endpoint_name = stores_vector_store.get("endpoint_name")
    store_index_name = stores_vector_store.get("index_name")
    store_columns = stores_vector_store.get("columns")

    @mlflow.trace()
    def general(state: AgentState, config: AgentConfig) -> dict[str, BaseMessage]:
        """
        Handle general customer service queries and analytical questions.
        
        Args:
            state: Current agent state containing messages and context
            config: Agent configuration parameters
            
        Returns:
            Dictionary with updated agent state
        """
        llm: LanguageModelLike = ChatDatabricks(model=model, temperature=0.1)

        prompt_template: PromptTemplate = PromptTemplate.from_template(prompt)
        configurable: dict[str, Any] = {
            "user_id": state["user_id"],
            "store_num": state["store_num"],
        }
        system_prompt: str = prompt_template.format(**configurable)

        # Initialize tools list
        tools = []
        
        # Add Genie query tool for complex analytical questions
        genie_tool = create_genie_query_tool(model_config)
        tools.append(genie_tool)
        logger.debug("Added Genie query tool to general agent")
        
        # Add customer profile intelligence tool for customer insights
        customer_intelligence_tool = create_customer_profile_intelligence_tool(warehouse_id, model_config, llm)
        tools.append(customer_intelligence_tool)
        logger.debug("Added customer profile intelligence tool to general agent")
        
        # Add store search tool if vector search is configured
        if store_endpoint_name and store_index_name and store_columns:
            store_search_tool = find_store_details_by_location_tool(
                endpoint_name=store_endpoint_name,
                index_name=store_index_name,
                columns=store_columns,
                k=10,
            )
            tools.append(store_search_tool)
            logger.debug("Added store vector search tool to general agent")
        
        # Create the agent with tools
        agent: CompiledStateGraph = create_react_agent(
            model=llm,
            prompt=system_prompt,
            tools=tools,
        )

        # Apply guardrails if configured and available
        if GUARDRAILS_AVAILABLE:
            for guardrail_definition in guardrails:
                guardrail: CompiledStateGraph = reflection_guardrail(guardrail_definition)
                agent = with_guardrails(agent, guardrail)
        elif guardrails:
            logger.warning("Guardrails configured but guardrails module not available")

        logger.debug(f"General agent created with {len(tools)} tools and guardrails")
        return agent

    return general 