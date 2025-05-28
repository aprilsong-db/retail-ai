"""
Tools Package

This package contains all tool creation functions and utilities for the Retail AI system.
Tools are organized by category: product tools, inventory tools, store tools, etc.
"""

from retail_ai.tools.factory import ToolFactory
from retail_ai.tools.employee import (
    create_find_top_employees_by_department_tool,
    create_find_personal_shopping_associates_tool,
    create_department_extraction_tool,
    create_find_employee_manager_tool,
    create_task_assignment_tool,
    create_task_extraction_tool,
)
from retail_ai.tools.inventory import (
    create_find_inventory_by_sku_tool,
    create_find_store_inventory_by_sku_tool,
    create_place_item_hold_tool,
)
from retail_ai.tools.product import (
    create_find_product_by_sku_tool,
    create_product_classification_tool,
    create_product_comparison_tool,
    create_sku_extraction_tool,
    find_product_details_by_description_tool,
    create_similar_products_recommendation_tool,
)
from retail_ai.tools.store import (
    create_find_store_by_number_tool,
    create_store_number_extraction_tool,
    find_store_details_by_location_tool,
)
from retail_ai.tools.external import (
    create_genie_tool,
    search_tool,
)
from retail_ai.tools.vector_search import (
    create_vector_search_tool,
)
from retail_ai.tools.unity_catalog import (
    create_uc_tools,
    find_allowable_classifications,
)
from retail_ai.tools.customer import (
    create_find_upcoming_customer_appointments_tool,
    create_get_customer_details_tool,
    create_customer_preparation_summary_tool,
    create_customer_profile_intelligence_tool,
    create_stylist_notification_tool,
    create_inventory_preselection_tool,
    create_appointment_preparation_workflow_tool,
    create_real_time_styling_assistant_tool,
)

__all__ = [
    # Factory
    "ToolFactory",
    
    # Product tools
    "create_find_product_by_sku_tool",
    "create_product_classification_tool",
    "create_product_comparison_tool",
    "create_sku_extraction_tool",
    "find_product_details_by_description_tool",
    "create_similar_products_recommendation_tool",
    
    # Inventory tools
    "create_find_inventory_by_sku_tool",
    "create_find_store_inventory_by_sku_tool",
    "create_place_item_hold_tool",
    
    # Store tools
    "create_find_store_by_number_tool",
    "create_store_number_extraction_tool",
    "find_store_details_by_location_tool",
    
    # Employee tools
    "create_find_top_employees_by_department_tool",
    "create_find_personal_shopping_associates_tool",
    "create_department_extraction_tool",
    "create_find_employee_manager_tool",
    "create_task_assignment_tool",
    "create_task_extraction_tool",
    
    # External tools
    "create_genie_tool",
    "search_tool",
    
    # Vector search tools
    "create_vector_search_tool",
    
    # Unity Catalog tools
    "create_uc_tools",
    "find_allowable_classifications",
    
    # Customer tools
    "create_find_upcoming_customer_appointments_tool",
    "create_get_customer_details_tool",
    "create_customer_preparation_summary_tool",
    "create_customer_profile_intelligence_tool",
    "create_stylist_notification_tool",
    "create_inventory_preselection_tool",
    "create_appointment_preparation_workflow_tool",
    "create_real_time_styling_assistant_tool",
] 