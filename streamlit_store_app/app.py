"""Streamlit Store Companion App."""

import os
from dotenv import load_dotenv
import streamlit as st
from components import load_css
from components.homepage import show_homepage
from utils.config import load_config
from utils.store_context import init_store_context, show_context_selector

def init_app():
    """Initialize the application."""
    load_dotenv()
    
    # Load and store config in session state
    if "config" not in st.session_state:
        st.session_state.config = load_config()
    
    load_css()

def show_home():
    """Display the modular card-based home page."""
    # Check if we have the minimum required context
    if not st.session_state.get('user_role'):
        st.warning("Please select a role from the sidebar to continue")
        return
    
    if not st.session_state.get('store_id'):
        st.warning("Store context not initialized. Please refresh the page.")
        return

    show_homepage()

def main():
    """Main application entry point."""
    try:
        st.set_page_config(
            page_title="BrickMate",
            page_icon="🏪",
            layout="wide"
        )

        init_app()
        init_store_context()
        show_context_selector()
        show_home()
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        if os.getenv("DEBUG", "false").lower() == "true":
            st.exception(e)

if __name__ == "__main__":
    main()
