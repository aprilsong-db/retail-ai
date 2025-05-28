"""
Customer Tools

This module contains tool creation functions for customer operations including
finding upcoming appointments, customer preparation details, and styling preferences.
Designed for store managers to quickly prepare for important customer visits.
"""

import mlflow
import pandas as pd
from datetime import datetime, timedelta
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.sql import StatementResponse, StatementState
from langchain_core.tools import tool
from langchain_core.language_models import LanguageModelLike
from loguru import logger
from typing import Callable, Optional
from mlflow.models import ModelConfig


def create_find_upcoming_customer_appointments_tool(warehouse_id: str, config: ModelConfig) -> Callable:
    """
    Create a Unity Catalog tool for finding upcoming customer appointments.
    
    This tool helps managers quickly identify customers with upcoming appointments
    and get essential preparation information for providing exceptional service.
    
    Args:
        warehouse_id: Databricks warehouse ID for query execution
        config: Model configuration containing catalog and database names
        
    Returns:
        A callable tool function that finds upcoming customer appointments
    """
    logger.debug("create_find_upcoming_customer_appointments_tool")
    
    # Get catalog and database names from config
    catalog_name = config.get("catalog_name")
    database_name = config.get("database_name")
    
    @tool
    def find_upcoming_customer_appointments(store_id: str = None, hours_ahead: int = 24) -> tuple:
        """
        Find upcoming customer appointments for preparation.
        
        This tool retrieves customers with appointments in the specified timeframe,
        providing managers with essential information to prepare for important customer visits.
        
        Args:
            store_id (str, optional): Specific store ID to search within (e.g., "101", "102", "103").
                                    If not provided, searches across all stores.
            hours_ahead (int): Number of hours ahead to look for appointments (default: 24)
            
        Returns:
            tuple: Customer appointment data including:
                - customer_id, customer_name, preferred_name, customer_tier
                - appointment_date, appointment_type, appointment_purpose
                - preferred_stylist_name, style_preferences, budget_range
                - preparation_notes, service_notes, special_occasions
                - requires_manager_greeting, customer_alerts
                - satisfaction_score, total_lifetime_spend
        """
        logger.debug(f"find_upcoming_customer_appointments: store_id={store_id}, hours_ahead={hours_ahead}")
        
        # Build WHERE clause based on parameters
        where_conditions = [
            f"next_appointment_date <= TIMESTAMPADD(HOUR, {hours_ahead}, CURRENT_TIMESTAMP())"
        ]
        
        if store_id:
            where_conditions.append(f"preferred_store_id = '{store_id}'")
        
        where_clause = "WHERE " + " AND ".join(where_conditions)
        
        # Execute query using the pre-built view
        sql_query = f"""
            SELECT 
                customer_id,
                customer_name,
                preferred_name,
                customer_tier,
                store_name,
                preferred_stylist_name,
                next_appointment_date,
                appointment_type,
                appointment_purpose,
                style_preferences,
                budget_range,
                preparation_notes,
                special_occasions,
                service_notes,
                requires_manager_greeting,
                customer_alerts,
                satisfaction_score,
                total_lifetime_spend,
                last_visit_date,
                ROUND((UNIX_TIMESTAMP(next_appointment_date) - UNIX_TIMESTAMP(CURRENT_TIMESTAMP())) / 3600, 1) as hours_until_appointment
            FROM {catalog_name}.{database_name}.upcoming_customer_appointments
            {where_clause}
            ORDER BY next_appointment_date ASC
            LIMIT 10
        """
        
        # Get workspace client and execute query
        w = WorkspaceClient()
        
        response: StatementResponse = w.statement_execution.execute_statement(
            warehouse_id=warehouse_id,
            statement=sql_query,
            wait_timeout="30s",
        )

        if response.status.state != StatementState.SUCCEEDED:
            logger.error(f"Query failed: {response.status}")
            return ()

        # Convert results to DataFrame and then to tuple
        if response.result and response.result.data_array:
            df = pd.DataFrame(
                response.result.data_array,
                columns=[col.name for col in response.result.manifest.schema.columns]
            )
            logger.debug(f"Found {len(df)} upcoming customer appointments")
            return tuple(df.to_dict('records'))
        
        return ()
    
    return find_upcoming_customer_appointments


def create_get_customer_details_tool(warehouse_id: str, config: ModelConfig) -> Callable:
    """
    Create a Unity Catalog tool for getting detailed customer information.
    
    This tool provides comprehensive customer details for managers to prepare
    for customer visits and ensure personalized service.
    
    Args:
        warehouse_id: Databricks warehouse ID for query execution
        config: Model configuration containing catalog and database names
        
    Returns:
        A callable tool function that gets customer details
    """
    logger.debug("create_get_customer_details_tool")
    
    # Get catalog and database names from config
    catalog_name = config.get("catalog_name")
    database_name = config.get("database_name")
    
    @tool
    def get_customer_details(customer_name: str = None, customer_id: str = None) -> tuple:
        """
        Get comprehensive customer details for appointment preparation.
        
        This tool retrieves detailed information about a specific customer,
        including preferences, history, and special requirements for personalized service.
        
        Args:
            customer_name (str, optional): Customer name to search for (partial matches supported)
            customer_id (str, optional): Specific customer ID to look up
            
        Returns:
            tuple: Comprehensive customer information including:
                - Basic info: name, customer tier, contact preferences
                - Styling preferences: style, sizes, colors, brands, budget
                - Service history: sessions, satisfaction, feedback
                - Special requirements: dietary, accessibility, cultural considerations
                - Upcoming appointment details and preparation notes
                - Family information and gift history
        """
        logger.debug(f"get_customer_details: customer_name={customer_name}, customer_id={customer_id}")
        
        # Build WHERE clause based on parameters
        where_conditions = []
        
        if customer_id:
            where_conditions.append(f"customer_id = '{customer_id}'")
        elif customer_name:
            where_conditions.append(f"LOWER(customer_name) LIKE LOWER('%{customer_name}%')")
        else:
            return ()  # Need at least one search parameter
        
        where_clause = "WHERE " + " AND ".join(where_conditions)
        
        # Execute query using the preparation summary view
        sql_query = f"""
            SELECT 
                customer_id,
                customer_name,
                preferred_name,
                customer_tier,
                store_name,
                next_appointment_date,
                appointment_type,
                appointment_purpose,
                style_preferences,
                size_information,
                color_preferences,
                brand_preferences,
                budget_range,
                preparation_notes,
                service_notes,
                special_occasions,
                dietary_restrictions,
                accessibility_needs,
                requires_manager_greeting,
                customer_alerts,
                preferred_stylist_name,
                stylist_experience,
                stylist_rating,
                customer_satisfaction,
                total_lifetime_spend,
                average_transaction_value,
                last_visit_date,
                visit_frequency,
                days_since_last_visit,
                hours_until_appointment
            FROM {catalog_name}.{database_name}.customer_preparation_summary
            {where_clause}
            ORDER BY next_appointment_date ASC
            LIMIT 5
        """
        
        # Get workspace client and execute query
        w = WorkspaceClient()
        
        response: StatementResponse = w.statement_execution.execute_statement(
            warehouse_id=warehouse_id,
            statement=sql_query,
            wait_timeout="30s",
        )

        if response.status.state != StatementState.SUCCEEDED:
            logger.error(f"Query failed: {response.status}")
            return ()

        # Convert results to DataFrame and then to tuple
        if response.result and response.result.data_array:
            df = pd.DataFrame(
                response.result.data_array,
                columns=[col.name for col in response.result.manifest.schema.columns]
            )
            logger.debug(f"Found {len(df)} customer records")
            return tuple(df.to_dict('records'))
        
        return ()
    
    return get_customer_details


def create_customer_preparation_summary_tool(warehouse_id: str, config: ModelConfig, llm: LanguageModelLike) -> Callable:
    """
    Create a tool that provides an AI-generated preparation summary for customers.
    
    This tool uses an LLM with a predefined prompt to generate intelligent, context-aware
    preparation summaries for upcoming customer visits across various scenarios.
    
    Args:
        warehouse_id: Databricks warehouse ID for query execution
        config: Model configuration containing catalog and database names
        llm: Language model for generating intelligent summaries
        
    Returns:
        A callable tool function that creates AI-powered preparation summaries
    """
    logger.debug("create_customer_preparation_summary_tool")
    
    # Get catalog and database names from config
    catalog_name = config.get("catalog_name")
    database_name = config.get("database_name")
    
    # Define the preparation summary prompt
    PREPARATION_SUMMARY_PROMPT = """You are an expert retail customer service manager creating a preparation summary for an upcoming customer visit. Your goal is to help store staff provide exceptional, personalized service.

Based on the customer data provided, create a comprehensive preparation summary that includes:

1. **Customer Overview**: Key facts about the customer (name, tier, value, satisfaction)
2. **Appointment Context**: What they're coming for and when
3. **Key Preparation Points**: Specific actions staff should take (use emojis for visual clarity)
4. **Service Requirements**: Special needs, preferences, and protocols
5. **Styling/Product Preferences**: What they like and what to focus on
6. **Conversation Starters**: Personal details that can enhance the interaction
7. **Success Factors**: What will make this visit exceptional

**Context Guidelines:**
- For personal shopping appointments: Focus on styling preferences, budget, and creating a personalized experience
- For consultations: Emphasize expertise, problem-solving, and building trust
- For regular visits: Highlight relationship building and consistent service
- For new customers: Focus on making a great first impression and learning preferences
- For high-tier customers: Emphasize premium service, attention to detail, and exceeding expectations

**Tone**: Professional, actionable, and focused on customer success. Use clear formatting to make the summary easy to scan quickly.

**Customer Data:**
{customer_data}

Generate a preparation summary that will help staff deliver outstanding service for this specific customer and appointment context."""

    @tool
    def create_customer_preparation_summary(customer_name: str, context: str = "general visit") -> str:
        """
        Generate an AI-powered preparation summary for a customer visit.
        
        This tool creates an intelligent, context-aware summary with key preparation points
        for upcoming customer appointments, ensuring exceptional service delivery across
        various scenarios including personal shopping, consultations, and regular visits.
        
        Args:
            customer_name (str): Name of the customer
            context (str): Context for the visit (e.g., "personal shopping appointment", 
                          "wardrobe consultation", "general visit", "new customer")
            
        Returns:
            str: AI-generated preparation summary with:
                - Customer overview and tier information
                - Appointment details and timing
                - Key preparation points with actionable items
                - Service requirements and preferences
                - Styling/product preferences
                - Conversation starters and success factors
        """
        logger.debug(f"create_customer_preparation_summary: customer_name={customer_name}, context={context}")
        
        # Get customer details first
        get_details = create_get_customer_details_tool(warehouse_id, config)
        customer_data = get_details.invoke({"customer_name": customer_name})
        
        if not customer_data:
            return f"No customer found with name containing '{customer_name}'. Please check the spelling or try a different search term."
        
        customer = customer_data[0]  # Get first match
        
        # Format customer data for the LLM prompt
        formatted_data = f"""
Customer Name: {customer.get('customer_name')} (prefers: {customer.get('preferred_name', 'N/A')})
Customer Tier: {customer.get('customer_tier', 'N/A')}
Store: {customer.get('store_name', 'N/A')}

Appointment Information:
- Date/Time: {customer.get('next_appointment_date', 'N/A')}
- Type: {customer.get('appointment_type', 'N/A')}
- Purpose: {customer.get('appointment_purpose', 'N/A')}
- Hours Until: {customer.get('hours_until_appointment', 'N/A')}
- Context: {context}

Customer Value & History:
- Lifetime Spend: ${customer.get('total_lifetime_spend', 0):,.2f}
- Average Transaction: ${customer.get('average_transaction_value', 0):,.2f}
- Satisfaction Score: {customer.get('customer_satisfaction', 'N/A')}/5.0
- Visit Frequency: {customer.get('visit_frequency', 'N/A')}
- Days Since Last Visit: {customer.get('days_since_last_visit', 'N/A')}
- Styling Sessions: {customer.get('stylist_experience', 'N/A')}

Preferences & Requirements:
- Style Preferences: {customer.get('style_preferences', 'N/A')}
- Size Information: {customer.get('size_information', 'N/A')}
- Color Preferences: {customer.get('color_preferences', 'N/A')}
- Brand Preferences: {customer.get('brand_preferences', 'N/A')}
- Budget Range: {customer.get('budget_range', 'N/A')}

Service Requirements:
- Manager Greeting Required: {customer.get('requires_manager_greeting', False)}
- Preferred Stylist: {customer.get('preferred_stylist_name', 'N/A')}
- Special Alerts: {customer.get('customer_alerts', 'N/A')}
- Dietary Restrictions: {customer.get('dietary_restrictions', 'N/A')}
- Accessibility Needs: {customer.get('accessibility_needs', 'N/A')}

Additional Notes:
- Preparation Notes: {customer.get('preparation_notes', 'N/A')}
- Service Notes: {customer.get('service_notes', 'N/A')}
- Special Occasions: {customer.get('special_occasions', 'N/A')}
"""
        
        # Generate the summary using the LLM
        try:
            prompt = PREPARATION_SUMMARY_PROMPT.format(customer_data=formatted_data)
            summary = llm.invoke(prompt)
            
            # Extract content if it's a message object
            if hasattr(summary, 'content'):
                summary_text = summary.content
            else:
                summary_text = str(summary)
            
            logger.debug(f"Generated preparation summary for {customer_name}")
            return summary_text
            
        except Exception as e:
            logger.error(f"Error generating summary with LLM: {e}")
            # Fallback to basic summary if LLM fails
            return f"""
Error generating AI summary. Basic customer information:

**{customer.get('customer_name')} ({customer.get('customer_tier')} tier)**
- Appointment: {customer.get('next_appointment_date')} - {customer.get('appointment_type')}
- Purpose: {customer.get('appointment_purpose')}
- Budget: {customer.get('budget_range')}
- Preferred Stylist: {customer.get('preferred_stylist_name', 'None specified')}
- Manager Greeting: {'Required' if customer.get('requires_manager_greeting') else 'Not required'}
- Special Notes: {customer.get('customer_alerts', 'None')}

Please contact technical support for assistance with the AI summary feature.
"""
    
    return create_customer_preparation_summary 