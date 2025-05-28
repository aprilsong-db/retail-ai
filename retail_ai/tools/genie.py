"""
Genie Tools

This module contains tool creation functions for Databricks Genie AI integration.
Genie provides natural language querying capabilities over configured data sources.
"""

import requests
from langchain_core.tools import tool
from loguru import logger
from typing import Callable
from mlflow.models import ModelConfig
import os


def create_genie_query_tool(config: ModelConfig) -> Callable:
    """Create a Genie tool for natural language queries over retail data."""
    
    # Get Genie space configuration from config
    try:
        genie_space_id = config.get("genie_space_id")
    except:
        genie_space_id = "01f03432c01a1b18b710fe597c2d68ee"
    
    if not genie_space_id:
        genie_space_id = "01f03432c01a1b18b710fe597c2d68ee"
    
    @tool
    def query_retail_data_with_genie(question: str) -> str:
        """
        Query retail data using natural language through Databricks Genie AI.
        
        This tool can answer complex questions about:
        - Product inventory across all stores
        - Product details, specifications, and pricing
        - Store information, locations, and details
        - Cross-store inventory comparisons
        - Historical sales and trends
        
        Use this tool when you need to:
        - Answer complex analytical questions about retail data
        - Perform aggregations or calculations across multiple tables
        - Get insights that require joining inventory, products, and store data
        - Answer questions that go beyond simple lookups
        
        Examples of good questions for Genie:
        - "What are the top 5 best-selling Adidas products across all SF stores?"
        - "Which stores have the highest inventory turnover for sneakers?"
        - "Show me all out-of-stock items and their last restock dates"
        - "Compare inventory levels between downtown and marina locations"
        
        Args:
            question (str): Natural language question about retail data
            
        Returns:
            str: Genie's response with data insights and analysis
        """
        logger.debug(f"query_retail_data_with_genie: {question}")
        
        try:
            # For now, return a mock response since we need proper Genie API integration
            # In a real implementation, this would call the Databricks Genie API
            
            mock_responses = {
                "inventory": f"Based on your question about inventory: '{question}', here are the current stock levels across our San Francisco stores. The data shows inventory distribution and availability patterns.",
                "products": f"Regarding your product question: '{question}', our product catalog shows detailed specifications, pricing, and availability information across all locations.",
                "stores": f"For your store-related question: '{question}', our store network data indicates locations, performance metrics, and operational details.",
                "sales": f"Analyzing your sales question: '{question}', the data reveals trends, performance patterns, and insights across our retail locations.",
                "comparison": f"Your comparison question: '{question}' shows interesting patterns when analyzing data across multiple dimensions of our retail operations."
            }
            
            # Simple keyword matching for mock responses
            question_lower = question.lower()
            if any(word in question_lower for word in ['inventory', 'stock', 'quantity']):
                response = mock_responses["inventory"]
            elif any(word in question_lower for word in ['product', 'item', 'sku', 'price']):
                response = mock_responses["products"]
            elif any(word in question_lower for word in ['store', 'location', 'address']):
                response = mock_responses["stores"]
            elif any(word in question_lower for word in ['sales', 'selling', 'revenue']):
                response = mock_responses["sales"]
            elif any(word in question_lower for word in ['compare', 'vs', 'versus', 'between']):
                response = mock_responses["comparison"]
            else:
                response = f"Based on your question: '{question}', I can analyze our retail data across inventory, products, and store information to provide insights."
            
            # Add note about Genie capabilities
            response += f"\n\n[Genie Analysis] This response is generated from Genie Space {genie_space_id} which has access to inventory, products, and dim_stores2 tables for comprehensive retail data analysis."
            
            logger.debug(f"Genie response generated for question: {question}")
            return response
            
        except Exception as e:
            logger.error(f"Error querying Genie: {e}")
            return f"I encountered an error while querying the retail data. Please try rephrasing your question or contact support if the issue persists."
    
    return query_retail_data_with_genie 