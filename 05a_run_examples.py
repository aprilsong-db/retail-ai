# Databricks notebook source

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages
import mlflow
from mlflow import MlflowClient


mlflow.set_registry_uri('databricks-uc')

# Get model details from config
model_name = config.get("app").get("registered_model_name")

# Get the latest model version using MlflowClient (same approach as 07_deploy_agent.py)
client: MlflowClient = MlflowClient()

# Get all versions and find the latest
versions = client.search_model_versions(f"name='{model_name}'")
if not versions:
    raise ValueError(f"No versions found for model {model_name}")

latest_version = max(versions, key=lambda v: int(v.version))
print(f"Latest model version: {latest_version.version}")

# Load the specific latest version
latest_model = mlflow.pyfunc.load_model(f"models:/{model_name}/{latest_version.version}")

# COMMAND ----------

# MAGIC %md
# MAGIC # BrickMart Retail AI - Demo Script Examples
# MAGIC ## Store Associate & Manager Demo Scenarios
# MAGIC 
# MAGIC This notebook demonstrates the exact queries from the BrickMart demo scripts:
# MAGIC 
# MAGIC ### Store Associate Demo (Sarah):
# MAGIC - **Scene 1**: Initial inventory check for black Adidas Gazelles  
# MAGIC - **Scene 2**: Recommendation request for similar sneakers  
# MAGIC - **Scene 3**: Cross-store inventory check  
# MAGIC - **Scene 4**: Hold request and notifications  
# MAGIC 
# MAGIC ### Manager Demo (Maria - Personal Stylist):
# MAGIC - **Customer Profile**: Victoria Chen VIP customer details  
# MAGIC - **Appointment Prep**: What to prepare for styling appointment  
# MAGIC - **Real-time Support**: Modern blazer suggestions during appointment  

# COMMAND ----------

# MAGIC %md
# MAGIC ## Demo Script Examples - Store Associate (Sarah)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scene 1: Initial Inventory Check
# MAGIC **Customer**: "Excuse me, do you have the Adidas Gazelle sneakers in black?"  
# MAGIC **Sarah**: "Hey Assistant, can you check if we have Adidas Gazelle sneakers in black at our Downtown Market location?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_initial_inventory_check")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scene 2: Recommendation Request
# MAGIC **Customer**: "I really wanted black. What else do you have that's similar?"  
# MAGIC **Sarah**: "Assistant, can you recommend similar sneakers to the black Gazelles that we have in stock?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_recommendation_request")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scene 3: Cross-Store Inventory Check
# MAGIC **Customer**: "I really have my heart set on the black Gazelles. Are there other stores nearby that might have them?"  
# MAGIC **Sarah**: "Assistant, can you check which nearby stores have black Gazelles in stock?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_cross_store_check")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scene 4: Hold Request
# MAGIC **Customer**: "The Marina store is perfect! Could you have them hold a pair in size 10 for me?"  
# MAGIC **Sarah**: "Assistant, can you place a hold on black Gazelles, size 10, at Marina Market for this customer?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_hold_request")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scene 4: Directions and Notifications
# MAGIC **Customer**: "Yes, please send me the directions and sign me up for the restock notifications."  
# MAGIC **Sarah**: "Assistant, please send directions to Marina Market and set up restock notifications for black Gazelles."

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_directions_notifications")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Demo Script Examples - Personal Stylist (Maria)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Customer Profile Request
# MAGIC **Maria**: "Show me everything I need to know about Victoria Chen."

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_customer_profile")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Appointment Preparation
# MAGIC **Maria**: "What should I prepare for Victoria's appointment today?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_appointment_preparation")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Real-time Styling Support
# MAGIC **Maria**: "Victoria likes the navy blazer but wants something more modern. Suggestions?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("demo_styling_support")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Brand Rep Product Education Demo - Nike Air Max Training

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brand Rep Demo Question 1: Nike Customer Intelligence
# MAGIC **Marcus**: "Nike brand representative is coming to train us on Air Max SC. What should I know about our customers who buy Nike?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

# Brand Rep Demo Question 1 - Nike Customer Intelligence
input_example: dict[str, Any] = {
    'messages': [
        {
            'role': 'user',
            'content': 'Nike brand representative is coming to train us on Air Max SC. What should I know about our customers who buy Nike?'
        }
    ],
    'custom_inputs': {
        'configurable': {
            'thread_id': '1',
            'user_id': 'marcus.associate',
            'store_num': 101
        }
    }
}
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brand Rep Demo Question 2: Product Performance Analytics
# MAGIC **Marcus**: "Show me how Nike Air Max products perform at our store."

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

# Brand Rep Demo Question 2 - Product Performance Analytics
input_example: dict[str, Any] = {
    'messages': [
        {
            'role': 'user',
            'content': 'Show me how Nike Air Max products perform at our store.'
        }
    ],
    'custom_inputs': {
        'configurable': {
            'thread_id': '1',
            'user_id': 'marcus.associate',
            'store_num': 101
        }
    }
}
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brand Rep Demo Question 3: Competitive Intelligence
# MAGIC **Marcus**: "What do customers say when they choose Adidas over Nike?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

# Brand Rep Demo Question 3 - Competitive Intelligence
input_example: dict[str, Any] = {
    'messages': [
        {
            'role': 'user',
            'content': 'What do customers say when they choose Adidas over Nike?'
        }
    ],
    'custom_inputs': {
        'configurable': {
            'thread_id': '1',
            'user_id': 'marcus.associate',
            'store_num': 101
        }
    }
}
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brand Rep Demo Question 4: Product Comparison
# MAGIC **Marcus**: "How does Air Max SC cushioning compare to our top-selling Air Max 90?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

# Brand Rep Demo Question 4 - Product Comparison
input_example: dict[str, Any] = {
    'messages': [
        {
            'role': 'user',
            'content': 'How does Air Max SC cushioning compare to our top-selling Air Max 90?'
        }
    ],
    'custom_inputs': {
        'configurable': {
            'thread_id': '1',
            'user_id': 'marcus.associate',
            'store_num': 101
        }
    }
}
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brand Rep Demo Question 5: Nike Product Positioning
# MAGIC **Marcus**: "How should I position Nike Air Max products to different customer segments?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

# Brand Rep Demo Question 5 - Product Positioning
input_example: dict[str, Any] = {
    'messages': [
        {
            'role': 'user',
            'content': 'How should I position Nike Air Max products to different customer segments based on our sales data?'
        }
    ],
    'custom_inputs': {
        'configurable': {
            'thread_id': '1',
            'user_id': 'marcus.associate',
            'store_num': 101
        }
    }
}
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brand Rep Demo Question 6: Sales Objection Handling
# MAGIC **Marcus**: "What are the most common objections to Nike products and how do successful associates handle them?"

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

# Brand Rep Demo Question 6 - Sales Objection Handling
input_example: dict[str, Any] = {
    'messages': [
        {
            'role': 'user',
            'content': 'What are the most common objections to Nike products and how do successful associates handle them?'
        }
    ],
    'custom_inputs': {
        'configurable': {
            'thread_id': '1',
            'user_id': 'marcus.associate',
            'store_num': 101
        }
    }
}
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC # Additional Examples - Supporting Demo Scenarios

# COMMAND ----------

# MAGIC %md
# MAGIC ## Product Tools Examples - Adidas Footwear

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Gazelle Product Lookup by SKU

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("product_by_sku_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Gazelle Product Lookup by UPC

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("product_by_upc_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Inventory Tools Examples - San Francisco Stores

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Samba Inventory Across All SF Stores

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("inventory_by_sku_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Samba Inventory by UPC (All SF Locations)

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("inventory_by_upc_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Gazelle at Downtown Market Store

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("store_inventory_by_sku_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Gazelle at Marina Market Store (by UPC)

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("store_inventory_by_upc_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## San Francisco Store Information

# COMMAND ----------

# MAGIC %md
# MAGIC ### Downtown Market & Marina Market Details

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("store_by_number_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mission Market Hours & Adidas Rewards

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("store_hours_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### San Francisco Store Search (Vector Search)

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("store_location_search_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Customer Service Examples - SF Stores

# COMMAND ----------

# MAGIC %md
# MAGIC ### Customer Appointments at SF Stores

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("customer_appointments_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Customer Footwear Preferences

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("customer_details_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sneaker Styling Appointment Preparation

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("customer_preparation_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### VIP Customer Sneaker Styling

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("vip_customer_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Employee Management - SF Footwear Department

# COMMAND ----------

# MAGIC %md
# MAGIC ### Top Footwear Department Performers

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("top_employees_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sneaker Styling Associates in SF

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("personal_shopping_associates_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Employee Manager at Downtown Market

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("employee_manager_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Gazelle BOPIS Task Assignment

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("task_assignment_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### SF Footwear Department Performance

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("department_performance_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Adidas Sneaker Recommendations

# COMMAND ----------

# MAGIC %md
# MAGIC ### Retro Suede Style Recommendations

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("recommendation_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Alternative to Out-of-Stock Gazelle

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("alternative_recommendation_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Adidas Gazelle vs Samba Comparison

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("comparison_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Sneaker Image Comparison

# COMMAND ----------

from typing import Any, Sequence
from rich import print as pprint

from pathlib import Path
from langchain_core.messages import HumanMessage, convert_to_messages
from agent_as_code import app, config
from retail_ai.models import process_messages
from retail_ai.messages import convert_to_langchain_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("comparison_image_example")
pprint(input_example)

messages: Sequence[HumanMessage] = convert_to_langchain_messages(input_example["messages"])
custom_inputs = input_example["custom_inputs"]

process_messages(
  app=app, 
  messages=messages, 
  custom_inputs=custom_inputs
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## General San Francisco Store Information

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("general_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Adidas Sneaker Care & Maintenance

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("diy_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Adidas Samba Order Tracking

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("orders_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Adidas Sneaker Image Analysis

# COMMAND ----------

from typing import Any, Sequence
from rich import print as pprint

from pathlib import Path
from langchain_core.messages import HumanMessage, convert_to_messages
from agent_as_code import app, config
from retail_ai.models import process_messages
from retail_ai.messages import convert_to_langchain_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("product_image_example")
pprint(input_example)

messages: Sequence[HumanMessage] = convert_to_langchain_messages(input_example["messages"])
custom_inputs = input_example["custom_inputs"]

process_messages(
  app=app, 
  messages=messages, 
  custom_inputs=custom_inputs
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Real Data Examples - Specific Adidas Products

# COMMAND ----------

# MAGIC %md
# MAGIC ### Black Gazelle Out of Stock at Downtown

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("out_of_stock_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Samba UPC Lookup

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("specific_upc_lookup_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Gazelle SKU Lookup

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("specific_sku_lookup_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Samba Cross-Store Inventory

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("cross_store_inventory_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Downtown vs Marina Adidas Selection

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("store_comparison_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Size & Fit Examples

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Gazelle Size 9.5 Availability

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("size_availability_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Samba Colors at Mission Market

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("color_availability_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## San Francisco Style Consultation

# COMMAND ----------

# MAGIC %md
# MAGIC ### Versatile Adidas for SF Lifestyle

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("style_consultation_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas for SF Weather & Terrain

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("sf_weather_styling_example")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Streaming Examples - Adidas Focus

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Recommendation with Streaming

# COMMAND ----------

from typing import Any
from agent_as_code import app, config
from retail_ai.models import process_messages_stream

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("recommendation_example")
pprint(input_example)

for event in process_messages_stream(app=app, **input_example):
  print(event.choices[0].delta.content, end="", flush=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adidas Inventory with Streaming

# COMMAND ----------

from typing import Any
from agent_as_code import app, config
from retail_ai.models import process_messages_stream

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("inventory_by_sku_example")
pprint(input_example)

for event in process_messages_stream(app=app, **input_example):
  print(event.choices[0].delta.content, end="", flush=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Gazelle vs Samba Comparison with Streaming

# COMMAND ----------

from typing import Any
from agent_as_code import app, config
from retail_ai.models import process_messages_stream

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("comparison_example")
pprint(input_example)

for event in process_messages_stream(app=app, **input_example):
  print(event.choices[0].delta.content, end="", flush=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Model Prediction Examples - Demo Script Scenarios

# COMMAND ----------

# MAGIC %md
# MAGIC ### Model Prediction - Demo Scene 1 (Initial Check)

# COMMAND ----------

input_example: dict[str, Any] = {
  'messages': [
    {
      'role': 'user',
      'content': 'Hey Assistant, can you check if we have Adidas Gazelle sneakers in black at our Downtown Market location?'
    }
  ],
  'custom_inputs': {
      'configurable': {
        'thread_id': '1',
        'user_id': 'sarah.associate',
        'store_num': 101
      }
    }
  }
pprint(input_example)

# Make prediction using loaded model
response = latest_model.predict(input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Model Prediction - Demo Scene 2 (Recommendations)

# COMMAND ----------

input_example: dict[str, Any] = {
  'messages': [
    {
      'role': 'user',
      'content': 'Assistant, can you recommend similar sneakers to the black Gazelles that we have in stock?'
    }
  ],
  'custom_inputs': {
      'configurable': {
        'thread_id': '1',
        'user_id': 'sarah.associate',
        'store_num': 101
      }
    }
  }
pprint(input_example)

response = latest_model.predict(input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Model Prediction - Demo Scene 3 (Cross-Store Check)

# COMMAND ----------

input_example: dict[str, Any] = {
  'messages': [
    {
      'role': 'user',
      'content': 'Assistant, can you check which nearby stores have black Gazelles in stock?'
    }
  ],
  'custom_inputs': {
      'configurable': {
        'thread_id': '1',
        'user_id': 'sarah.associate',
        'store_num': 101
      }
    }
  }
pprint(input_example)

response = latest_model.predict(input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Model Prediction - Manager Demo (Customer Profile)

# COMMAND ----------

input_example: dict[str, Any] = {
  'messages': [
    {
      'role': 'user',
      'content': 'Show me everything I need to know about Victoria Chen.'
    }
  ],
  'custom_inputs': {
      'configurable': {
        'thread_id': '1',
        'user_id': 'maria.stylist',
        'store_num': 101
      }
    }
  }
pprint(input_example)

response = latest_model.predict(input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Brand Rep Demo Examples from Config

# COMMAND ----------

# MAGIC %md
# MAGIC ### Config Example: Nike Customer Intelligence

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("brand_rep_nike_customers")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Config Example: Product Performance Analytics

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("brand_rep_product_performance")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Config Example: Competitive Analysis

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("brand_rep_competitive_analysis")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Config Example: Product Comparison

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("brand_rep_product_comparison")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Config Example: Product Positioning

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("brand_rep_positioning")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Config Example: Objection Handling

# COMMAND ----------

from typing import Any
from rich import print as pprint
from agent_as_code import app, config
from retail_ai.models import process_messages

examples: dict[str, Any] = config.get("app").get("examples")
input_example: dict[str, Any] = examples.get("brand_rep_objection_handling")
pprint(input_example)

response = process_messages(app=app, **input_example)
pprint(response)

