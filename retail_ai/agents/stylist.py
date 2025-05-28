"""
Stylist Agent

This module contains the stylist agent that handles personal styling appointments,
customer preparation, and real-time styling assistance.
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
from retail_ai.tools.customer import (
    create_customer_profile_intelligence_tool,
    create_stylist_notification_tool,
    create_inventory_preselection_tool,
    create_appointment_preparation_workflow_tool,
    create_real_time_styling_assistant_tool,
    create_get_customer_details_tool,
)
from retail_ai.tools.product import create_similar_products_recommendation_tool

# Optional imports for guardrails
try:
    from retail_ai.guardrails import reflection_guardrail, with_guardrails
    GUARDRAILS_AVAILABLE = True
except ImportError:
    GUARDRAILS_AVAILABLE = False


def stylist_agent(model_config: ModelConfig) -> AgentCallable:
    """
    Create a stylist agent that handles personal styling appointments and customer preparation.

    This agent specializes in:
    - Personal styling appointment preparation and notifications
    - AI-powered inventory pre-selection for customers
    - Real-time styling assistance during appointments
    - Customer profile intelligence and insights
    - Appointment workflow coordination

    Args:
        model_config: Model configuration containing stylist agent settings

    Returns:
        An agent callable function that handles styling workflows
    """
    model: str = model_config.get("agents").get("stylist").get("model").get("name")
    prompt: str = model_config.get("agents").get("stylist").get("prompt")
    guardrails: Sequence[dict[str, Any]] = (
        model_config.get("agents").get("stylist").get("guardrails") or []
    )

    warehouse_id: str = (
        model_config.get("resources")
        .get("warehouses")
        .get("shared_endpoint_warehouse")
        .get("warehouse_id")
    )

    @mlflow.trace()
    def stylist(state: AgentState, config: AgentConfig) -> dict[str, BaseMessage]:
        """
        Handle personal styling appointments and customer preparation workflows.
        
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
        
        # Add customer profile intelligence tool
        customer_intelligence_tool = create_customer_profile_intelligence_tool(warehouse_id, model_config, llm)
        tools.append(customer_intelligence_tool)
        logger.debug("Added customer profile intelligence tool to stylist agent")
        
        # Add stylist notification tool
        notification_tool = create_stylist_notification_tool(warehouse_id, model_config, llm)
        tools.append(notification_tool)
        logger.debug("Added stylist notification tool to stylist agent")
        
        # Add inventory pre-selection tool
        preselection_tool = create_inventory_preselection_tool(warehouse_id, model_config, llm)
        tools.append(preselection_tool)
        logger.debug("Added inventory pre-selection tool to stylist agent")
        
        # Add appointment preparation workflow tool
        workflow_tool = create_appointment_preparation_workflow_tool(warehouse_id, model_config, llm)
        tools.append(workflow_tool)
        logger.debug("Added appointment preparation workflow tool to stylist agent")
        
        # Add real-time styling assistant tool
        styling_assistant_tool = create_real_time_styling_assistant_tool(warehouse_id, model_config, llm)
        tools.append(styling_assistant_tool)
        logger.debug("Added real-time styling assistant tool to stylist agent")
        
        # Add customer details tool for basic customer lookup
        customer_details_tool = create_get_customer_details_tool(warehouse_id, model_config)
        tools.append(customer_details_tool)
        logger.debug("Added customer details tool to stylist agent")
        
        # Add similar products tool for styling recommendations
        similar_products_tool = create_similar_products_recommendation_tool(warehouse_id, model_config)
        tools.append(similar_products_tool)
        logger.debug("Added similar products tool to stylist agent")
        
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

        logger.debug(f"Stylist agent created with {len(tools)} tools and guardrails")
        return agent

    return stylist 