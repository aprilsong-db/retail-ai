"""Store context management utilities."""

import streamlit as st
from datetime import datetime
from utils.database import query, get_stores
from utils.config import load_config

def init_store_context():
    """Initialize store context in session state."""
    # Load configuration
    config = st.session_state.config
    
    # Initialize store context
    if "store_id" not in st.session_state:
        st.session_state.store_id = None
    if "store_name" not in st.session_state:
        st.session_state.store_name = None
    if "user_role" not in st.session_state:
        st.session_state.user_role = None
    if "show_context_switcher" not in st.session_state:
        st.session_state.show_context_switcher = True
    if "store_details" not in st.session_state:
        st.session_state.store_details = None
    

def toggle_context_switcher():
    """Toggle the visibility of the context switcher."""
    st.session_state.show_context_switcher = not st.session_state.show_context_switcher

def check_permission(permission: str) -> bool:
    """Check if current user role has a specific permission."""
    if not st.session_state.user_role:
        return False
    return st.session_state.config["roles"][st.session_state.user_role].get(permission, False)

def format_store_details(store_details: dict) -> str:
    """Format store details for display."""
    # Get employee name from config
    employee_name = st.session_state.config["employees"][st.session_state.user_role]["name"]
    role_title = st.session_state.user_role.replace('_', ' ').title()
    
    # Handle 24/7 stores
    if store_details.get('is_24_hours', False):
        hours_display = "24/7"
    else:
        current_day = datetime.now().strftime('%A').lower()
        hours = store_details['hours'][current_day]
        hours_display = f"{hours['open']} - {hours['close']}"
    
    # Remove "BrickMart" from store name for display
    clean_store_name = store_details['name'].replace("BrickMart ", "").strip()
    
    return (
        f"**Working as:** {employee_name} ({role_title})\n\n"
        f"**Store:** {clean_store_name}\n"
        f"**Type:** {store_details['type'].title()}\n"
        f"**Address:** {store_details['address']}\n"
        f"**Location:** {store_details['city']}, {store_details['state']} {store_details['zip_code']}\n"
        f"**Hours Today:** {hours_display}\n"
        f"**Size:** {store_details['size_sqft']:,} sq ft\n"
        f"**Rating:** {'⭐' * int(store_details['rating'])}"
    )

def show_context_selector():
    """Display the store context selector."""
    # Show context switcher panel if activated
    if st.session_state.show_context_switcher:
        with st.sidebar:
            st.markdown("### Store Context")
            
            # Get stores from database
            try:
                stores_df = get_stores()
                if stores_df.empty:
                    st.error("No stores available. Please check your database connection.")
                    return
                
                # Convert DataFrame to list of dicts for easier handling
                stores = stores_df.to_dict('records')
                
                # Create display names with format "City, State - Store Name" and remove "BrickMart"
                store_display_options = []
                store_display_to_store = {}
                
                for store in stores:
                    # Remove "BrickMart" from store name
                    clean_name = store["name"].replace("BrickMart ", "").strip()
                    display_name = f"{store['city']}, {store['state']} - {clean_name}"
                    store_display_options.append(display_name)
                    store_display_to_store[display_name] = store
                
                roles = list(st.session_state.config["roles"].keys())
                
                # Find current selection index
                current_selection_index = None
                if st.session_state.get("store_name"):
                    current_store_name = st.session_state.store_name
                    for i, (display_name, store) in enumerate(store_display_to_store.items()):
                        if store["name"] == current_store_name:
                            current_selection_index = i
                            break
                
                # Store selection
                selected_store_display = st.selectbox(
                    "Select Store:",
                    options=store_display_options,
                    index=current_selection_index,
                    placeholder="Choose a store..."
                )
                
                # Role selection
                selected_role = st.selectbox(
                    "Select Role:",
                    options=roles,
                    index=None if not st.session_state.get("user_role") else 
                          roles.index(st.session_state.user_role),
                    placeholder="Choose your role..."
                )
                
                # Apply button
                if st.button("Apply", type="primary"):
                    if selected_store_display and selected_role:
                        # Find selected store using the display name
                        store = store_display_to_store.get(selected_store_display)
                        if store:
                            st.session_state.store_id = store["id"]
                            st.session_state.store_name = store["name"]
                            st.session_state.user_role = selected_role
                            st.session_state.store_details = store
                            st.session_state.show_context_switcher = True  # Keep switcher visible
                            st.rerun()
                        else:
                            st.error("Selected store not found.")
                    else:
                        st.warning("Please select both store and role")
                        
            except Exception as e:
                st.error(f"Error loading stores: {str(e)}")
                st.info("Please check your database configuration.")

    # Show current context
    if st.session_state.store_name and st.session_state.user_role:
        st.sidebar.success(format_store_details(st.session_state.store_details))
    else:
        st.sidebar.warning("Please select both store and role to continue") 