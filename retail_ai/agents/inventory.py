"""
Inventory Agent

This module contains the inventory agent that handles inventory queries,
stock level checks, and store-specific inventory information.
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
from retail_ai.tools import (
    create_find_inventory_by_sku_tool,
    create_find_store_inventory_by_sku_tool,
    find_product_details_by_description_tool,
    find_store_details_by_location_tool,
    create_similar_products_recommendation_tool,
)
from retail_ai.tools.inventory import (
    create_find_inventory_by_sku_tool,
    create_find_store_inventory_by_sku_tool,
    create_find_nearby_stores_inventory_tool,
    create_place_item_hold_tool
)
from retail_ai.types import AgentCallable

# Optional imports for guardrails
try:
    from retail_ai.guardrails import reflection_guardrail, with_guardrails
    GUARDRAILS_AVAILABLE = True
except ImportError:
    GUARDRAILS_AVAILABLE = False


def inventory_agent(model_config: ModelConfig) -> AgentCallable:
    """
    Create an inventory agent that handles inventory and stock level queries.

    This agent specializes in inventory-related tasks including stock level checks,
    store-specific inventory queries, and availability information.

    Args:
        model_config: Model configuration containing inventory agent settings

    Returns:
        An agent callable function that handles inventory queries
    """
    model: str = model_config.get("agents").get("inventory").get("model").get("name")
    prompt: str = model_config.get("agents").get("inventory").get("prompt")
    guardrails: Sequence[dict[str, Any]] = (
        model_config.get("agents").get("inventory").get("guardrails") or []
    )

    warehouse_id: str = (
        model_config.get("resources")
        .get("warehouses")
        .get("shared_endpoint_warehouse")
        .get("warehouse_id")
    )

    # Get vector search configuration for products
    products_vector_store = model_config.get("resources").get("vector_stores").get("products_vector_store")
    product_endpoint_name = products_vector_store.get("endpoint_name")
    product_index_name = products_vector_store.get("index_name")
    product_columns = products_vector_store.get("columns")

    # Get vector search configuration for stores
    stores_vector_store = model_config.get("resources").get("vector_stores").get("store_vector_store")
    store_endpoint_name = stores_vector_store.get("endpoint_name")
    store_index_name = stores_vector_store.get("index_name")
    store_columns = stores_vector_store.get("columns")

    @mlflow.trace()
    def inventory(state: AgentState, config: AgentConfig) -> dict[str, BaseMessage]:
        """
        Handle inventory-related queries and stock level checks.
        
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

        # Create inventory-specific tools
        tools = [
            create_find_inventory_by_sku_tool(warehouse_id, model_config),
            create_find_store_inventory_by_sku_tool(warehouse_id, model_config),
        ]

        # Add vector search tools for product and store lookup
        if product_endpoint_name and product_index_name and product_columns:
            product_search_tool = find_product_details_by_description_tool(
                endpoint_name=product_endpoint_name,
                index_name=product_index_name,
                columns=product_columns,
                k=10,
            )
            tools.append(product_search_tool)
            logger.debug("Added product vector search tool to inventory agent")

        if store_endpoint_name and store_index_name and store_columns:
            store_search_tool = find_store_details_by_location_tool(
                endpoint_name=store_endpoint_name,
                index_name=store_index_name,
                columns=store_columns,
                k=10,
            )
            tools.append(store_search_tool)
            logger.debug("Added store vector search tool to inventory agent")

        # Add nearby stores inventory tool
        nearby_stores_inventory_tool = create_find_nearby_stores_inventory_tool(warehouse_id, config)
        tools.append(nearby_stores_inventory_tool)
        logger.debug("Added nearby stores inventory tool to inventory agent")

        # Add item hold placement tool
        place_hold_tool = create_place_item_hold_tool(warehouse_id, model_config)
        tools.append(place_hold_tool)
        logger.debug("Added place item hold tool to inventory agent")

        # Add similar products recommendation tool for suggesting alternatives when out of stock
        if product_endpoint_name and product_index_name and product_columns and warehouse_id:
            similar_products_tool = create_similar_products_recommendation_tool(
                endpoint_name=product_endpoint_name,
                index_name=product_index_name,
                columns=product_columns,
                warehouse_id=warehouse_id,
                model_config=model_config,
                k=5,  # Return top 5 similar products
            )
            tools.append(similar_products_tool)
            logger.debug("Added similar products recommendation tool to inventory agent")

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

        logger.debug("Inventory agent created with tools and guardrails")
        return agent

    return inventory 