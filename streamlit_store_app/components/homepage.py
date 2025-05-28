"""Homepage components for the retail store employee iPad app."""

import streamlit as st
from datetime import datetime, timedelta
from utils.database import query, get_stores
from utils.store_context import check_permission
from components.metrics import display_metric_card, display_alert
from components.chat import show_chat_container
import streamlit_modal as modal
import pandas as pd
from streamlit_card import card

def show_notifications_modal():
    """Display notifications in an expandable modal."""
    # Initialize notification state
    if "show_notifications" not in st.session_state:
        st.session_state.show_notifications = False
    
    # Notification button with count badge
    notification_count = 4  # Mock count
    
    col1, col2, col3 = st.columns([1, 1, 8])
    with col1:
        if st.button(f"🔔 {notification_count}", key="notifications_toggle", help="View notifications"):
            st.session_state.show_notifications = not st.session_state.show_notifications
    
    # Show notifications modal if toggled
    if st.session_state.show_notifications:
        with st.expander("📢 Notifications", expanded=True):
            # Categorized notifications
            st.markdown("#### 🚨 Urgent")
            urgent_notifications = [
                {"message": "Security system maintenance in 30 minutes - Electronics section", "time": "5 min ago"},
                {"message": "VIP customer arriving at 2 PM - Personal shopping assistance needed", "time": "15 min ago"}
            ]
            
            for notif in urgent_notifications:
                st.markdown(f"""
                    <div class="notification-item urgent">
                        <div class="notification-message">{notif["message"]}</div>
                        <div class="notification-time">{notif["time"]}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("#### ⚠️ Important")
            important_notifications = [
                {"message": "New designer collection arriving tomorrow - Prepare display area", "time": "1 hour ago"},
                {"message": "Staff meeting moved to 3 PM in conference room", "time": "2 hours ago"}
            ]
            
            for notif in important_notifications:
                st.markdown(f"""
                    <div class="notification-item important">
                        <div class="notification-message">{notif["message"]}</div>
                        <div class="notification-time">{notif["time"]}</div>
                    </div>
                """, unsafe_allow_html=True)

def show_kpi_summary():
    """Display condensed KPI dashboard for store managers."""
    st.markdown("### 📊 Store Performance")
    
    # Mock retail data
    today_sales = 28750.00
    yesterday_sales = 24320.00
    sales_change = ((today_sales - yesterday_sales) / yesterday_sales) * 100
    
    pending_orders = 15
    completed_orders = 89
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="kpi-summary-card sales">
                <div class="kpi-icon">💰</div>
                <div class="kpi-value">${today_sales:,.0f}</div>
                <div class="kpi-label">Today's Sales</div>
                <div class="kpi-change positive">+{sales_change:.1f}%</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="kpi-summary-card orders">
                <div class="kpi-icon">📦</div>
                <div class="kpi-value">{completed_orders}</div>
                <div class="kpi-label">Orders Complete</div>
                <div class="kpi-change">{pending_orders} pending</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="kpi-summary-card traffic">
                <div class="kpi-icon">👥</div>
                <div class="kpi-value">247</div>
                <div class="kpi-label">Customers Today</div>
                <div class="kpi-change">Peak: 2-4 PM</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="kpi-summary-card conversion">
                <div class="kpi-icon">📈</div>
                <div class="kpi-value">68%</div>
                <div class="kpi-label">Conversion Rate</div>
                <div class="kpi-change positive">+5% vs avg</div>
            </div>
        """, unsafe_allow_html=True)

def show_inventory_summary():
    """Display condensed inventory status for all employees."""
    st.markdown("### 📊 Inventory Status")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="inventory-summary-card critical">
                <div class="inventory-icon">🚨</div>
                <div class="inventory-value">3</div>
                <div class="inventory-label">Critical Stock</div>
                <div class="inventory-detail">Designer Jeans, iPhone Cases</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="inventory-summary-card low">
                <div class="inventory-icon">⚠️</div>
                <div class="inventory-value">12</div>
                <div class="inventory-label">Low Stock</div>
                <div class="inventory-detail">Seasonal items</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="inventory-summary-card good">
                <div class="inventory-icon">✅</div>
                <div class="inventory-value">892</div>
                <div class="inventory-label">Well Stocked</div>
                <div class="inventory-detail">Core inventory</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="inventory-summary-card new">
                <div class="inventory-icon">🆕</div>
                <div class="inventory-value">24</div>
                <div class="inventory-label">New Arrivals</div>
                <div class="inventory-detail">Fall collection</div>
            </div>
        """, unsafe_allow_html=True)

def show_manager_summary_cards():
    """Display summary cards for store managers with navigation."""
    st.markdown("### 🎯 Quick Access")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Daily Operations", key="daily_ops", use_container_width=True):
            st.switch_page("pages/daily_operations.py")
        
        st.markdown("""
            <div class="summary-card operations">
                <div class="summary-stats">
                    <div class="stat-item">
                        <span class="stat-value">5/8</span>
                        <span class="stat-label">Tasks Complete</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">2</span>
                        <span class="stat-label">Urgent Items</span>
                    </div>
                </div>
                <div class="summary-preview">
                    • Morning inventory ✅<br>
                    • Vendor delivery 🔄<br>
                    • Staff meeting ⏳
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("👥 Team Insights", key="team_insights", use_container_width=True):
            st.switch_page("pages/team_insights.py")
        
        st.markdown("""
            <div class="summary-card team">
                <div class="summary-stats">
                    <div class="stat-item">
                        <span class="stat-value">12/15</span>
                        <span class="stat-label">Staff Present</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">94%</span>
                        <span class="stat-label">Avg Performance</span>
                    </div>
                </div>
                <div class="summary-preview">
                    🏆 Top: Sarah Chen (98%)<br>
                    ⚠️ Coverage gap: 3-4 PM<br>
                    📅 3 shift changes today
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("📊 Detailed Inventory", key="detailed_inventory", use_container_width=True):
            st.switch_page("pages/inventory.py")
        
        st.markdown("""
            <div class="summary-card inventory">
                <div class="summary-stats">
                    <div class="stat-item">
                        <span class="stat-value">$2.1M</span>
                        <span class="stat-label">Total Value</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">15</span>
                        <span class="stat-label">Reorder Needed</span>
                    </div>
                </div>
                <div class="summary-preview">
                    📱 Electronics: 95% stocked<br>
                    👗 Apparel: 87% stocked<br>
                    👟 Footwear: 92% stocked
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_associate_homepage_with_chat(chat_modal, chat_notifications):
    """Display homepage content for store associates with integrated chat button."""
    # Create tabs with chat button on the same line
    col1, col2 = st.columns([8, 2])
    
    with col1:
        # Main content in tabs - fully tab-based experience
        tab1, tab2, tab3, tab4 = st.tabs(["🎯 My Work", "📅 Schedule", "🏷️ Products", "📊 Performance"])
    
    with col2:
        # Chat button aligned with tabs
        if chat_notifications > 0:
            button_text = f"💬 AI Assistant ({chat_notifications})"
        else:
            button_text = "💬 AI Assistant"
        
        if st.button(button_text, key="associate_chat_btn", type="primary", use_container_width=True):
            st.session_state.chat_notifications = 0
            chat_modal.open()
    
    # Tab content
    with tab1:
        show_my_work_tab()
    
    with tab2:
        show_schedule_tab()
    
    with tab3:
        show_products_tab()
    
    with tab4:
        show_performance_tab()

def show_associate_homepage():
    """Display homepage content for store associates with improved tab-based layout."""
    # Add custom CSS for better tab styling with stronger selectors
    st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px !important;
        padding: 12px 24px !important;
        background-color: #f8f9fa !important;
        border-radius: 8px 8px 0px 0px !important;
        border: 1px solid #dee2e6 !important;
        border-bottom: none !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        color: #495057 !important;
        transition: all 0.2s ease !important;
    }
    .stTabs [data-baseweb="tab"] p {
        font-size: 22px !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e9ecef !important;
        color: #212529 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #007bff !important;
        color: white !important;
        border-color: #007bff !important;
    }
    .stTabs [aria-selected="true"] p {
        color: white !important;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main content in tabs - fully tab-based experience with clean styling
    tab1, tab2, tab3, tab4 = st.tabs(["My Work", "Schedule", "Products", "Performance"])
    
    with tab1:
        show_my_work_tab()
    
    with tab2:
        show_schedule_tab()
    
    with tab3:
        show_products_tab()
    
    with tab4:
        show_performance_tab()

def show_my_work_tab():
    """Display the My Work tab with tasks and immediate priorities."""
    # Quick status bar at top
    st.markdown("#### 🎯 Current Status")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="quick-status-card active">
                <div class="status-icon">🟢</div>
                <div class="status-text">On Shift</div>
                <div class="status-detail">3h 37m left</div>
                <div class="assignment-info">
                    <div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.3); font-size: 16px; font-weight: 600;">
                        <div><strong>Assignment:</strong> Women's Fashion</div>
                        <div><strong>Section:</strong> Designer Area</div>
                        <div><strong>Coverage:</strong> Solo until 2 PM</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="quick-status-card tasks">
                <div class="status-icon">📋</div>
                <div class="status-text">7 Tasks</div>
                <div class="status-detail">3 high priority</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="quick-status-card inventory">
                <div class="status-icon">📦</div>
                <div class="status-text">Inventory</div>
                <div class="status-detail">3 critical items</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="quick-status-card notifications">
                <div class="status-icon">🔔</div>
                <div class="status-text">4 Alerts</div>
                <div class="status-detail">2 urgent</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### 🎯 Today's Priorities")
        
        # High priority tasks preview
        priority_tasks = [
            {"title": "BOPIS Order #B2024-0156", "customer": "Sarah Johnson", "due": "10:30 AM", "type": "BOPIS"},
            {"title": "Personal Shopping Appt", "customer": "Emma Rodriguez", "due": "2:00 PM", "type": "Service"},
            {"title": "Restock Designer Section", "location": "Floor 2", "due": "12:00 PM", "type": "Restock"}
        ]
        
        for task in priority_tasks:
            task_type_colors = {"BOPIS": "#007bff", "Service": "#6f42c1", "Restock": "#28a745"}
            st.markdown(f"""
                <div class="priority-task-preview">
                    <div class="task-preview-header">
                        <span class="task-preview-title">{task['title']}</span>
                        <span class="task-preview-type" style="background-color: {task_type_colors[task['type']]}">
                            {task['type']}
                        </span>
                    </div>
                    <div class="task-preview-details">
                        Due: {task['due']} • {task.get('customer', task.get('location', ''))}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        if st.button("📋 View All Tasks", key="view_all_tasks", use_container_width=True):
            st.switch_page("pages/my_tasks.py")
    
    with col2:
        st.markdown("#### 🚨 Quick Actions")
        
        # Quick action buttons
        if st.button("🛒 Check BOPIS Orders", use_container_width=True):
            st.switch_page("pages/my_tasks.py")
        
        if st.button("📦 Report Low Stock", use_container_width=True):
            st.info("Stock reporting form would open")
        
        if st.button("🤝 Request Help", use_container_width=True):
            st.info("Help request sent to manager")
        
        if st.button("☕ Take Break", use_container_width=True):
            st.success("Break started - timer activated")

def show_schedule_tab():
    """Display the Schedule tab with shift info and time tracking."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### ⏰ Current Shift")
        
        st.markdown("""
            <div class="shift-detail-card">
                <div class="shift-time-info">
                    <div class="shift-current-time">12:23 PM</div>
                    <div class="shift-progress">
                        <div class="shift-progress-bar">
                            <div class="shift-progress-fill" style="width: 55%"></div>
                        </div>
                        <div class="shift-progress-text">4h 23m worked • 3h 37m remaining</div>
                    </div>
                </div>
                <div class="shift-details">
                    <div><strong>Shift:</strong> 8:00 AM - 4:00 PM</div>
                    <div><strong>Break:</strong> 12:00 - 12:30 PM (Due now!)</div>
                    <div><strong>Department:</strong> Women's Fashion</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("📅 View Full Schedule", use_container_width=True):
            st.switch_page("pages/my_schedule.py")
    
    with col2:
        st.markdown("#### 📊 This Week")
        
        st.markdown("""
            <div class="week-overview-card">
                <div class="week-stats-grid">
                    <div class="week-stat">
                        <div class="week-stat-value">32/40</div>
                        <div class="week-stat-label">Hours</div>
                    </div>
                    <div class="week-stat">
                        <div class="week-stat-value">4/5</div>
                        <div class="week-stat-label">Days</div>
                    </div>
                    <div class="week-stat">
                        <div class="week-stat-value">94%</div>
                        <div class="week-stat-label">Performance</div>
                    </div>
                    <div class="week-stat">
                        <div class="week-stat-value">$2,847</div>
                        <div class="week-stat-label">Sales</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📝 Upcoming")
        upcoming_items = [
            {"day": "Tomorrow", "shift": "8 AM - 4 PM", "dept": "Electronics"},
            {"day": "Friday", "shift": "9 AM - 5 PM", "dept": "Women's Fashion"},
            {"day": "Saturday", "shift": "OFF", "dept": ""}
        ]
        
        for item in upcoming_items:
            if item["shift"] == "OFF":
                st.markdown(f"""
                    <div class="new-item-preview">
                        <div class="new-item-name">🏖️ {item['day']}</div>
                        <div class="new-item-details">Day Off</div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="new-item-preview">
                        <div class="new-item-name">📅 {item['day']}</div>
                        <div class="new-item-details">{item['shift']} - {item['dept']}</div>
                    </div>
                """, unsafe_allow_html=True)

def show_products_tab():
    """Display the Products tab with promotions and product info."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔥 Active Promotions")
        
        promotions = [
            {"name": "Fall Fashion Sale", "discount": "40% off", "ends": "End of week"},
            {"name": "Designer Handbags", "discount": "25% off", "ends": "Tomorrow"},
            {"name": "Tech Accessories", "discount": "Buy 2 Get 1", "ends": "3 days"}
        ]
        
        for promo in promotions:
            st.markdown(f"""
                <div class="promo-preview-card">
                    <div class="promo-preview-header">
                        <span class="promo-preview-name">{promo['name']}</span>
                        <span class="promo-preview-discount">{promo['discount']}</span>
                    </div>
                    <div class="promo-preview-ends">Ends: {promo['ends']}</div>
                </div>
            """, unsafe_allow_html=True)
        
        if st.button("🏷️ View All Promotions", use_container_width=True):
            st.switch_page("pages/products_promotions.py")
    
    with col2:
        st.markdown("#### 🆕 New This Week")
        
        new_items = [
            {"name": "iPhone 15 Pro Cases", "category": "Electronics", "location": "E3"},
            {"name": "Winter Coats", "category": "Women's Apparel", "location": "W2"},
            {"name": "Designer Sneakers", "category": "Footwear", "location": "F4"}
        ]
        
        for item in new_items:
            st.markdown(f"""
                <div class="new-item-preview">
                    <div class="new-item-name">{item['name']}</div>
                    <div class="new-item-details">{item['category']} • {item['location']}</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("#### 🔥 Trending")
        trending_items = [
            {"name": "Wireless Earbuds Pro", "growth": "+45%", "icon": "🎧"},
            {"name": "Oversized Blazers", "growth": "+60%", "icon": "👗"},
            {"name": "Minimalist Watches", "growth": "+35%", "icon": "⌚"}
        ]
        
        for item in trending_items:
            st.markdown(f"""
                <div class="new-item-preview">
                    <div class="new-item-name">{item['icon']} {item['name']}</div>
                    <div class="new-item-details">Growth: {item['growth']}</div>
                </div>
            """, unsafe_allow_html=True)

def show_performance_tab():
    """Display the Performance tab with personal metrics and achievements."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏆 Today's Performance")
        
        st.markdown("""
            <div class="performance-overview-card">
                <div class="performance-score">
                    <div class="performance-score-value">94%</div>
                    <div class="performance-score-label">Overall Score</div>
                </div>
                <div class="performance-metrics">
                    <div class="performance-metric">
                        <span class="metric-label">BOPIS Orders:</span>
                        <span class="metric-value">12 completed</span>
                    </div>
                    <div class="performance-metric">
                        <span class="metric-label">Customer Assists:</span>
                        <span class="metric-value">8 interactions</span>
                    </div>
                    <div class="performance-metric">
                        <span class="metric-label">Sales:</span>
                        <span class="metric-value">$2,450</span>
                    </div>
                    <div class="performance-metric">
                        <span class="metric-label">Customer Rating:</span>
                        <span class="metric-value">4.8/5 ⭐</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 🎯 Goals & Achievements")
        
        st.markdown("""
            <div class="goals-card">
                <div class="goal-item completed">
                    <span class="goal-icon">✅</span>
                    <span class="goal-text">Complete 10 BOPIS orders</span>
                </div>
                <div class="goal-item in-progress">
                    <span class="goal-icon">🔄</span>
                    <span class="goal-text">Assist 15 customers (8/15)</span>
                </div>
                <div class="goal-item pending">
                    <span class="goal-icon">⏳</span>
                    <span class="goal-text">Achieve $3,000 in sales</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 🏅 Recent Achievements")
        achievements = [
            {"name": "Customer Service Excellence", "icon": "🌟"},
            {"name": "Sales Target Exceeded", "icon": "💰"}, 
            {"name": "Speed Champion (BOPIS)", "icon": "⚡"}
        ]
        
        for achievement in achievements:
            st.markdown(f"""
                <div class="new-item-preview">
                    <div class="new-item-name">{achievement['icon']} {achievement['name']}</div>
                    <div class="new-item-details">Recently earned</div>
                </div>
            """, unsafe_allow_html=True)

def simulate_chat_notification():
    """Simulate receiving a chat notification (for demo purposes)."""
    if "chat_notifications" not in st.session_state:
        st.session_state.chat_notifications = 0
    
    # Only add notifications if chat is closed
    if not st.session_state.get("chat_window_open", False):
        st.session_state.chat_notifications += 1

def show_persistent_chat():
    """Display a floating chat icon in the lower right corner that opens a chat modal."""
    # Initialize chat state
    if "chat_notifications" not in st.session_state:
        st.session_state.chat_notifications = 0
    
    # Get current chat status
    chat_status = st.session_state.get("chat_status", "available")
    
    # Create notification badge HTML
    notification_badge = ""
    if st.session_state.chat_notifications > 0:
        notification_badge = f'''
        <span style="
            position: absolute;
            top: -5px;
            right: -5px;
            background: #ff4757;
            color: white;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            font-size: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        ">{st.session_state.chat_notifications}</span>
        '''
    
    # Create status indicator
    status_indicators = {
        "available": {"color": "#28a745", "pulse": ""},
        "typing": {"color": "#007bff", "pulse": "animation: pulse 1.5s infinite;"},
        "processing": {"color": "#ffc107", "pulse": "animation: pulse 1s infinite;"},
        "error": {"color": "#dc3545", "pulse": "animation: pulse 2s infinite;"}
    }
    
    status_info = status_indicators.get(chat_status, status_indicators["available"])
    
    # Status indicator dot HTML
    status_dot = f'''
    <span style="
        position: absolute;
        bottom: -2px;
        left: -2px;
        background: {status_info['color']};
        border: 2px solid white;
        border-radius: 50%;
        width: 16px;
        height: 16px;
        {status_info['pulse']}
    "></span>
    '''
    
    # Floating chat button HTML
    chat_button_html = f"""
    <style>
    @keyframes pulse {{
        0% {{ transform: scale(1); opacity: 1; }}
        50% {{ transform: scale(1.1); opacity: 0.7; }}
        100% {{ transform: scale(1); opacity: 1; }}
    }}
    </style>
    
    <div id="floating-chat-container" style="
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        z-index: 1000;
    ">
        <div style="
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
            position: relative;
        " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(0,0,0,0.2)'"
           onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'"
           onclick="document.getElementById('hidden-chat-btn').click()">
            💬
            {notification_badge}
            {status_dot}
        </div>
    </div>
    """
    
    # Display the floating chat icon
    st.markdown(chat_button_html, unsafe_allow_html=True)
    
    # Hidden button for modal trigger
    st.markdown("""
    <style>
    #hidden-chat-btn {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create the modal
    chat_modal = modal.Modal(
        title="🤖 AI Assistant",
        key="chat_modal",
        max_width=600,
        padding=20
    )
    
    # Hidden button to trigger modal
    if st.button("Open Chat", key="hidden_chat_btn", help="Open AI Assistant"):
        # Clear notifications when chat is opened
        st.session_state.chat_notifications = 0
        chat_modal.open()
    
    # Modal content
    if chat_modal.is_open():
        with chat_modal.container():
            # Get chat config with fallback
            chat_config = st.session_state.get("config", {}).get("chat", {
                "placeholder": "How can I help you today?",
                "max_tokens": 1000,
                "temperature": 0.7
            })
            
            # Show the chat container
            show_chat_container(chat_config)
    
    # Show appropriate homepage content based on user role (back to original functions)
    if user_role == "store_manager":
        # Show new tab-based manager homepage
        show_manager_homepage()
    else:
        # Show new tab-based associate homepage
        show_associate_homepage()

def show_manager_homepage_with_chat(chat_modal, chat_notifications):
    """Display tab-based homepage content for store managers with integrated chat button."""
    # Create tabs with chat button on the same line
    col1, col2 = st.columns([8, 2])
    
    with col1:
        # Main content in tabs - fully tab-based experience
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📊 Dashboard", "🎯 Operations", "👥 Team", "📦 Inventory", "📈 Analytics", "💡 Alerts"])
    
    with col2:
        # Chat button aligned with tabs
        if chat_notifications > 0:
            button_text = f"💬 AI Assistant ({chat_notifications})"
        else:
            button_text = "💬 AI Assistant"
        
        if st.button(button_text, key="manager_chat_btn", type="primary", use_container_width=True):
            st.session_state.chat_notifications = 0
            chat_modal.open()
    
    # Tab content
    with tab1:
        show_manager_dashboard_tab()
    
    with tab2:
        show_manager_alerts_tab()
    
    with tab3:
        show_manager_operations_tab()
    
    with tab4:
        show_manager_team_tab()
    
    with tab5:
        show_manager_inventory_tab()
    
    with tab6:
        show_manager_analytics_tab()

def show_manager_homepage():
    """Display tab-based homepage content for store managers."""
    # Add custom CSS for better tab styling with stronger selectors
    st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px !important;
        padding: 12px 24px !important;
        background-color: #f8f9fa !important;
        border-radius: 8px 8px 0px 0px !important;
        border: 1px solid #dee2e6 !important;
        border-bottom: none !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        color: #495057 !important;
        transition: all 0.2s ease !important;
    }
    .stTabs [data-baseweb="tab"] p {
        font-size: 22px !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e9ecef !important;
        color: #212529 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #007bff !important;
        color: white !important;
        border-color: #007bff !important;
    }
    .stTabs [aria-selected="true"] p {
        color: white !important;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main content in tabs - fully tab-based experience with clean styling
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Dashboard", "Alerts", "Operations", "Team", "Inventory", "Analytics"])
    
    with tab1:
        show_manager_dashboard_tab()
    
    with tab2:
        show_manager_alerts_tab()
    
    with tab3:
        show_manager_operations_tab()
    
    with tab4:
        show_manager_team_tab()
    
    with tab5:
        show_manager_inventory_tab()
    
    with tab6:
        show_manager_analytics_tab()

def show_manager_dashboard_tab():
    """Display the Dashboard tab with key metrics."""
    # Quick executive dashboard at top
    st.markdown("#### 📊 Store Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="manager-status-card sales">
                <div class="status-icon">💰</div>
                <div class="status-text">$28,750</div>
                <div class="status-detail">Today's Sales (+18%)</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="manager-status-card team">
                <div class="status-icon">👥</div>
                <div class="status-text">12/15</div>
                <div class="status-detail">Staff Present (94% avg)</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="manager-status-card operations">
                <div class="status-icon">📋</div>
                <div class="status-text">5/8</div>
                <div class="status-detail">Tasks Complete (2 urgent)</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="manager-status-card alerts">
                <div class="status-icon">🔔</div>
                <div class="status-text">4</div>
                <div class="status-detail">Active Alerts</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Today's Performance")
        
        st.markdown("""
            <div class="manager-dashboard-card">
                <div class="dashboard-metrics">
                    <div class="dashboard-metric">
                        <span class="metric-label">Sales Target:</span>
                        <span class="metric-value">96% ($28,750/$30,000)</span>
                        <span class="metric-trend positive">+18% vs yesterday</span>
                    </div>
                    <div class="dashboard-metric">
                        <span class="metric-label">Customer Traffic:</span>
                        <span class="metric-value">247 visitors</span>
                        <span class="metric-trend">Peak: 2-4 PM</span>
                    </div>
                    <div class="dashboard-metric">
                        <span class="metric-label">Conversion Rate:</span>
                        <span class="metric-value">68%</span>
                        <span class="metric-trend positive">+5% vs avg</span>
                    </div>
                    <div class="dashboard-metric">
                        <span class="metric-label">Avg Transaction:</span>
                        <span class="metric-value">$171.50</span>
                        <span class="metric-trend positive">+12% vs avg</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 📈 Performance Trends")
        
        st.markdown("""
            <div class="manager-dashboard-card">
                <div class="dashboard-metrics">
                    <div class="dashboard-metric">
                        <span class="metric-label">Weekly Sales:</span>
                        <span class="metric-value">$142,350</span>
                        <span class="metric-trend positive">+12% vs last week</span>
                    </div>
                    <div class="dashboard-metric">
                        <span class="metric-label">Monthly Target:</span>
                        <span class="metric-value">78% complete</span>
                        <span class="metric-trend positive">On track</span>
                    </div>
                    <div class="dashboard-metric">
                        <span class="metric-label">Customer Satisfaction:</span>
                        <span class="metric-value">4.7/5.0</span>
                        <span class="metric-trend positive">+0.2 vs last month</span>
                    </div>
                    <div class="dashboard-metric">
                        <span class="metric-label">Staff Efficiency:</span>
                        <span class="metric-value">94%</span>
                        <span class="metric-trend positive">+3% vs avg</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_manager_alerts_tab():
    """Display the Alerts tab with interactive counters and scrollable alert containers."""
    # Add custom CSS for scrollable alert containers and interactive elements
    st.markdown("""
    <style>
    .alerts-container {
        height: 400px;
        overflow-y: auto;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        background: #f8f9fa;
        margin-bottom: 1rem;
    }
    
    .alert-item {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 0.75rem;
        border-left: 4px solid;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
        cursor: pointer;
        position: relative;
    }
    
    .alert-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .alert-item.urgent {
        border-left-color: #dc3545;
        background: linear-gradient(90deg, #fff5f5 0%, white 10%);
    }
    
    .alert-item.important {
        border-left-color: #ffc107;
        background: linear-gradient(90deg, #fffbf0 0%, white 10%);
    }
    
    .alert-item.resolved {
        opacity: 0.6;
        background: #f8f9fa;
    }
    
    .alert-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    
    .alert-type {
        font-weight: 600;
        color: #495057;
        font-size: 0.9rem;
    }
    
    .alert-severity {
        background: #dc3545;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 600;
    }
    
    .alert-severity.important {
        background: #ffc107;
        color: #212529;
    }
    
    .alert-time {
        font-size: 0.75rem;
        color: #6c757d;
    }
    
    .alert-message {
        color: #495057;
        margin-bottom: 0.5rem;
        line-height: 1.4;
    }
    
    .alert-actions {
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize alert state
    if "resolved_alerts" not in st.session_state:
        st.session_state.resolved_alerts = set()
    if "show_alert_modal" not in st.session_state:
        st.session_state.show_alert_modal = False
    if "modal_alert_type" not in st.session_state:
        st.session_state.modal_alert_type = ""
    
    st.markdown("#### 🔔 Alert Management Center")
    
    # All alerts data
    all_alerts = [
        {"id": 0, "type": "Security Alert", "message": "Security system maintenance in 30 minutes - Electronics section", "severity": "urgent", "action": "Notify staff", "time": "5 min ago"},
        {"id": 1, "type": "VIP Customer", "message": "VIP customer arriving at 2 PM - Personal shopping assistance needed", "severity": "urgent", "action": "Prep personal shopper", "time": "15 min ago"},
        {"id": 2, "type": "Critical Stock", "message": "Designer Jeans - only 2 left", "severity": "urgent", "action": "Reorder now", "time": "20 min ago"},
        {"id": 3, "type": "Staff Coverage", "message": "Electronics understaffed 3-4 PM", "severity": "urgent", "action": "Find coverage", "time": "30 min ago"},
        {"id": 4, "type": "Delivery Update", "message": "New designer collection arriving tomorrow - Prepare display area", "severity": "important", "action": "Prep display area", "time": "1 hour ago"},
        {"id": 5, "type": "Schedule Change", "message": "Staff meeting moved to 3 PM in conference room", "severity": "important", "action": "Update team", "time": "2 hours ago"},
        {"id": 6, "type": "VIP Customer", "message": "Sarah Johnson arriving at 2 PM", "severity": "important", "action": "Prep personal shopper", "time": "2 hours ago"},
        {"id": 7, "type": "Delivery Delay", "message": "Designer collection delayed to 4:30 PM", "severity": "important", "action": "Update team", "time": "3 hours ago"}
    ]
    
    # Calculate real-time counters
    urgent_alerts = [a for a in all_alerts if a["severity"] == "urgent" and a["id"] not in st.session_state.resolved_alerts]
    important_alerts = [a for a in all_alerts if a["severity"] == "important" and a["id"] not in st.session_state.resolved_alerts]
    resolved_alerts = [a for a in all_alerts if a["id"] in st.session_state.resolved_alerts]
    total_active = len(urgent_alerts) + len(important_alerts)
    
    urgent_count = len(urgent_alerts)
    important_count = len(important_alerts)
    resolved_count = len(resolved_alerts)
    
    # Real-time counters with color-coded statistics using streamlit-card
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Urgent alerts card - Red theme
        urgent_clicked = card(
            title="🚨 Urgent",
            text=f"{urgent_count} alerts",
            styles={
                "card": {
                    "width": "100%",
                    "height": "200px",
                    "border-radius": "16px",
                    "box-shadow": "0 4px 20px rgba(220, 53, 69, 0.25)",
                    "background": "linear-gradient(135deg, #dc3545 0%, #c82333 100%)",
                    "border": "1px solid rgba(220, 53, 69, 0.3)",
                    "margin": "0",
                    "padding": "1.5rem",
                    "text-align": "center",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease"
                },
                "title": {
                    "font-size": "2.5rem",
                    "color": "white",
                    "font-weight": "700",
                    "margin-bottom": "0.5rem"
                },
                "text": {
                    "font-size": "1rem",
                    "color": "white",
                    "font-weight": "500",
                    "text-transform": "uppercase",
                    "letter-spacing": "0.5px"
                }
            },
            key="urgent_card"
        )
        
        if urgent_clicked:
            st.session_state.modal_alert_type = "urgent"
    
    with col2:
        # Important alerts card - Orange theme
        important_clicked = card(
            title="⚠️ Important",
            text=f"{important_count} alerts",
            styles={
                "card": {
                    "width": "100%",
                    "height": "200px",
                    "border-radius": "16px",
                    "box-shadow": "0 4px 20px rgba(255, 152, 0, 0.25)",
                    "background": "linear-gradient(135deg, #ff9800 0%, #f57c00 100%)",
                    "border": "1px solid rgba(255, 152, 0, 0.3)",
                    "margin": "0",
                    "padding": "1.5rem",
                    "text-align": "center",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease"
                },
                "title": {
                    "font-size": "2.5rem",
                    "color": "white",
                    "font-weight": "700",
                    "margin-bottom": "0.5rem"
                },
                "text": {
                    "font-size": "1rem",
                    "color": "white",
                    "font-weight": "500",
                    "text-transform": "uppercase",
                    "letter-spacing": "0.5px"
                }
            },
            key="important_card"
        )
        
        if important_clicked:
            st.session_state.modal_alert_type = "important"
    
    with col3:
        # Resolved alerts card - Green theme
        resolved_clicked = card(
            title="✅ Resolved",
            text=f"{resolved_count} alerts",
            styles={
                "card": {
                    "width": "100%",
                    "height": "200px",
                    "border-radius": "16px",
                    "box-shadow": "0 4px 20px rgba(40, 167, 69, 0.25)",
                    "background": "linear-gradient(135deg, #28a745 0%, #1e7e34 100%)",
                    "border": "1px solid rgba(40, 167, 69, 0.3)",
                    "margin": "0",
                    "padding": "1.5rem",
                    "text-align": "center",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease"
                },
                "title": {
                    "font-size": "2.5rem",
                    "color": "white",
                    "font-weight": "700",
                    "margin-bottom": "0.5rem"
                },
                "text": {
                    "font-size": "1rem",
                    "color": "white",
                    "font-weight": "500",
                    "text-transform": "uppercase",
                    "letter-spacing": "0.5px"
                }
            },
            key="resolved_card"
        )
        
        if resolved_clicked:
            st.session_state.modal_alert_type = "resolved"
    
    with col4:
        # Total active alerts card - Blue theme
        total_clicked = card(
            title="📊 Total Active",
            text=f"{total_active} alerts",
            styles={
                "card": {
                    "width": "100%",
                    "height": "200px",
                    "border-radius": "16px",
                    "box-shadow": "0 4px 20px rgba(0, 123, 255, 0.25)",
                    "background": "linear-gradient(135deg, #007bff 0%, #0056b3 100%)",
                    "border": "1px solid rgba(0, 123, 255, 0.3)",
                    "margin": "0",
                    "padding": "1.5rem",
                    "text-align": "center",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease"
                },
                "title": {
                    "font-size": "2.5rem",
                    "color": "white",
                    "font-weight": "700",
                    "margin-bottom": "0.5rem"
                },
                "text": {
                    "font-size": "1rem",
                    "color": "white",
                    "font-weight": "500",
                    "text-transform": "uppercase",
                    "letter-spacing": "0.5px"
                }
            },
            key="total_card"
        )
        
        if total_clicked:
            st.session_state.modal_alert_type = "all"
    
    # Set default alert type if none selected
    if not st.session_state.modal_alert_type:
        st.session_state.modal_alert_type = "all"
    
    # Always show the alert display area below the cards
    # Filter alerts based on current modal type
    if st.session_state.modal_alert_type == "urgent":
        display_alerts = urgent_alerts
        display_title = f"🚨 Urgent Alerts ({len(display_alerts)})"
    elif st.session_state.modal_alert_type == "important":
        display_alerts = important_alerts
        display_title = f"⚠️ Important Alerts ({len(display_alerts)})"
    elif st.session_state.modal_alert_type == "resolved":
        display_alerts = resolved_alerts
        display_title = f"✅ Resolved Alerts ({len(display_alerts)})"
    else:  # all
        display_alerts = urgent_alerts + important_alerts
        display_title = f"📊 All Active Alerts ({len(display_alerts)})"
    
    # Display the selected alert type
    st.markdown(f"### {display_title}")
    
    # Fixed height container with alert cards
    with st.container(height=400):
        if len(display_alerts) > 0:
            for alert in display_alerts:
                is_resolved = alert["id"] in st.session_state.resolved_alerts
                severity_class = "resolved" if is_resolved else alert["severity"]
                severity_label = "RESOLVED" if is_resolved else alert["severity"].upper()
                
                # Color coding for alert cards
                if alert["severity"] == "urgent":
                    border_color = "#dc3545"
                    bg_color = "#fff5f5" if not is_resolved else "#f8f9fa"
                    severity_bg = "#dc3545"
                    severity_text = "white"
                elif alert["severity"] == "important":
                    border_color = "#ffc107"
                    bg_color = "#fffbf0" if not is_resolved else "#f8f9fa"
                    severity_bg = "#ffc107"
                    severity_text = "#212529"
                else:
                    border_color = "#6c757d"
                    bg_color = "#f8f9fa"
                    severity_bg = "#6c757d"
                    severity_text = "white"
                
                # Alert card
                st.markdown(f"""
                <div style="
                    background: {bg_color};
                    border-left: 4px solid {border_color};
                    border-radius: 8px;
                    padding: 1rem;
                    margin-bottom: 0.75rem;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    opacity: {'0.6' if is_resolved else '1'};
                ">
                    <div style="
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        margin-bottom: 0.5rem;
                    ">
                        <span style="
                            font-weight: 600;
                            color: #495057;
                            font-size: 0.9rem;
                        ">{alert['type']}</span>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="
                                background: {severity_bg};
                                color: {severity_text};
                                padding: 0.2rem 0.5rem;
                                border-radius: 12px;
                                font-size: 0.7rem;
                                font-weight: 600;
                            ">{severity_label}</span>
                            <span style="
                                font-size: 0.75rem;
                                color: #6c757d;
                            ">{alert['time']}</span>
                        </div>
                    </div>
                    <div style="
                        color: #495057;
                        margin-bottom: 0.5rem;
                        line-height: 1.4;
                    ">{alert['message']}</div>
                    <div style="
                        color: #007bff;
                        font-size: 0.8rem;
                    ">→ {alert['action']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Action buttons for each alert
                if not is_resolved:
                    col1, col2, col3, col4 = st.columns([1, 1, 1, 6])
                    
                    with col1:
                        if st.button("✅", key=f"resolve_{alert['id']}", help="Mark as resolved"):
                            st.session_state.resolved_alerts.add(alert['id'])
                            st.rerun()
                    
                    with col2:
                        if st.button("📋", key=f"action_{alert['id']}", help="Take action"):
                            st.success(f"Taking action: {alert['action']}")
                    
                    with col3:
                        if st.button("👁️", key=f"details_{alert['id']}", help="View details"):
                            st.info(f"Alert details: {alert['message']}")
                else:
                    st.markdown("*This alert has been resolved*")
                
                st.markdown("---")
        else:
            st.info("No alerts to display.")
    
    # Action buttons at bottom
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📋 View All Operations", use_container_width=True):
            st.switch_page("pages/daily_operations.py")
    
    with col2:
        if st.button("📊 Generate Alert Report", use_container_width=True):
            st.info("Alert report would be generated")

def show_manager_operations_tab():
    """Display the Operations tab with daily priorities and tasks."""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### 🎯 Today's Priorities")
        
        operations = [
            {"task": "Morning inventory check", "status": "completed", "time": "08:00", "owner": "Sarah Chen"},
            {"task": "Staff meeting - Holiday prep", "status": "in_progress", "time": "09:30", "owner": "All Staff"},
            {"task": "Vendor delivery - Designer Collection", "status": "pending", "time": "11:00", "owner": "Mike Rodriguez"},
            {"task": "Weekly sales report review", "status": "pending", "time": "15:00", "owner": "Manager"},
            {"task": "Evening shift handover", "status": "pending", "time": "18:00", "owner": "Emma Wilson"}
        ]
        
        for op in operations:
            status_colors = {"completed": "#28a745", "in_progress": "#007bff", "pending": "#6c757d"}
            status_icons = {"completed": "✅", "in_progress": "🔄", "pending": "⏳"}
            
            st.markdown(f"""
                <div class="operation-preview-card">
                    <div class="operation-header">
                        <span class="operation-task">{op['task']}</span>
                        <span class="operation-time">{op['time']}</span>
                    </div>
                    <div class="operation-details">
                        <span style="color: {status_colors[op['status']]}">
                            {status_icons[op['status']]} {op['status'].replace('_', ' ').title()}
                        </span>
                        • Assigned to: {op['owner']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 📅 Quick Actions")
        
        if st.button("➕ Add Task", use_container_width=True):
            st.info("Task creation form would open")
        
        if st.button("📞 Call Staff", use_container_width=True):
            st.info("Staff contact list would open")
        
        if st.button("🚚 Track Deliveries", use_container_width=True):
            st.info("Delivery tracking would open")
        
        if st.button("📊 Generate Report", use_container_width=True):
            st.info("Report generator would open")
        
        st.markdown("#### 🕐 Store Hours")
        st.markdown("""
            <div class="store-hours-card">
                <div class="hours-today">
                    <div class="hours-label">Today:</div>
                    <div class="hours-time">8:00 AM - 9:00 PM</div>
                </div>
                <div class="hours-status">
                    <div class="status-open">🟢 Open</div>
                    <div class="hours-remaining">5h 37m remaining</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_manager_team_tab():
    """Display the Team tab with staff overview and performance."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👥 Team Status")
        
        team_members = [
            {"name": "Sarah Chen", "role": "Store Associate", "status": "active", "performance": 98, "location": "Women's Fashion"},
            {"name": "Mike Rodriguez", "role": "Store Associate", "status": "active", "performance": 95, "location": "Electronics"},
            {"name": "Emma Wilson", "role": "Store Associate", "status": "break", "performance": 92, "location": "Customer Service"},
            {"name": "James Park", "role": "Visual Merchandiser", "status": "active", "performance": 88, "location": "All Floors"},
            {"name": "Lisa Wong", "role": "Store Associate", "status": "off", "performance": 75, "location": "Men's Fashion"}
        ]
        
        for member in team_members:
            status_colors = {"active": "#28a745", "break": "#ffc107", "off": "#6c757d"}
            status_icons = {"active": "🟢", "break": "☕", "off": "🔴"}
            
            st.markdown(f"""
                <div class="team-member-card">
                    <div class="member-header">
                        <span class="member-name">{member['name']}</span>
                        <span class="member-status" style="color: {status_colors[member['status']]}">
                            {status_icons[member['status']]} {member['status'].title()}
                        </span>
                    </div>
                    <div class="member-details">
                        <div>{member['role']} • {member['location']}</div>
                        <div>Performance: {member['performance']}%</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        if st.button("👥 View Team Insights", use_container_width=True):
            st.switch_page("pages/team_insights.py")
    
    with col2:
        st.markdown("#### 📊 Team Metrics")
        
        st.markdown("""
            <div class="team-metrics-card">
                <div class="team-metric">
                    <span class="metric-label">Average Performance:</span>
                    <span class="metric-value">94%</span>
                </div>
                <div class="team-metric">
                    <span class="metric-label">Customer Satisfaction:</span>
                    <span class="metric-value">4.6/5</span>
                </div>
                <div class="team-metric">
                    <span class="metric-label">Tasks Completed:</span>
                    <span class="metric-value">47/52</span>
                </div>
                <div class="team-metric">
                    <span class="metric-label">Schedule Adherence:</span>
                    <span class="metric-value">98%</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### ⚠️ Team Alerts")
        team_alerts = [
            {"alert": "Coverage gap: 3-4 PM Electronics", "icon": "⚠️"},
            {"alert": "Sarah Chen: 42 hours this week", "icon": "⏰"},
            {"alert": "3 employees need safety training", "icon": "📚"}
        ]
        
        for alert in team_alerts:
            st.markdown(f"""
                <div class="new-item-preview">
                    <div class="new-item-name">{alert['icon']} Alert</div>
                    <div class="new-item-details">{alert['alert']}</div>
                </div>
            """, unsafe_allow_html=True)

def show_manager_inventory_tab():
    """Display the Inventory tab with stock levels and alerts."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📦 Inventory Overview")
        
        # Use the existing inventory summary but in a more compact format
        inventory_categories = [
            {"name": "Critical Stock", "count": 3, "items": ["Designer Jeans", "iPhone Cases", "Silk Scarves"], "color": "#dc3545"},
            {"name": "Low Stock", "count": 12, "items": ["Fall Jackets", "Wireless Headphones", "Boots"], "color": "#ffc107"},
            {"name": "Well Stocked", "count": 892, "items": ["Core inventory items"], "color": "#28a745"},
            {"name": "New Arrivals", "count": 24, "items": ["Winter Collection", "Holiday Items"], "color": "#6f42c1"}
        ]
        
        for category in inventory_categories:
            st.markdown(f"""
                <div class="inventory-category-card" style="border-left-color: {category['color']}">
                    <div class="category-header">
                        <span class="category-name">{category['name']}</span>
                        <span class="category-count">{category['count']}</span>
                    </div>
                    <div class="category-items">{', '.join(category['items'][:3])}</div>
                </div>
            """, unsafe_allow_html=True)
        
        if st.button("📊 Detailed Inventory", use_container_width=True):
            st.switch_page("pages/inventory.py")
    
    with col2:
        st.markdown("#### 💰 Inventory Value")
        
        st.markdown("""
            <div class="inventory-value-card">
                <div class="value-metric">
                    <span class="value-label">Total Inventory Value:</span>
                    <span class="value-amount">$2.1M</span>
                </div>
                <div class="value-metric">
                    <span class="value-label">Turnover Rate:</span>
                    <span class="value-amount">4.2x/year</span>
                </div>
                <div class="value-metric">
                    <span class="value-label">Reorder Needed:</span>
                    <span class="value-amount">15 items</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📈 Department Stock Levels")
        departments = [
            {"name": "Electronics", "level": 95, "color": "#28a745"},
            {"name": "Women's Fashion", "level": 87, "color": "#ffc107"},
            {"name": "Men's Fashion", "level": 92, "color": "#28a745"},
            {"name": "Footwear", "level": 78, "color": "#ffc107"}
        ]
        
        for dept in departments:
            st.markdown(f"""
                <div class="department-stock-bar">
                    <div class="dept-name">{dept['name']}</div>
                    <div class="stock-bar">
                        <div class="stock-fill" style="width: {dept['level']}%; background-color: {dept['color']}"></div>
                    </div>
                    <div class="stock-percentage">{dept['level']}%</div>
                </div>
            """, unsafe_allow_html=True)

def show_manager_analytics_tab():
    """Display the Analytics tab with trends and insights."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Sales Trends")
        
        st.markdown("""
            <div class="analytics-card">
                <div class="analytics-metric">
                    <span class="metric-label">Week-over-Week Growth:</span>
                    <span class="metric-value positive">+12.5%</span>
                </div>
                <div class="analytics-metric">
                    <span class="metric-label">Best Performing Category:</span>
                    <span class="metric-value">Electronics (+23%)</span>
                </div>
                <div class="analytics-metric">
                    <span class="metric-label">Peak Sales Hour:</span>
                    <span class="metric-value">2:00 - 4:00 PM</span>
                </div>
                <div class="analytics-metric">
                    <span class="metric-label">Return Rate:</span>
                    <span class="metric-value">2.8% (below target)</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 🎯 Goals Progress")
        goals = [
            {"name": "Monthly Sales Target", "progress": 78, "target": "$450K"},
            {"name": "Customer Satisfaction", "progress": 92, "target": "4.5/5"},
            {"name": "Inventory Turnover", "progress": 85, "target": "4.5x/year"}
        ]
        
        for goal in goals:
            color = "#28a745" if goal['progress'] >= 90 else "#ffc107" if goal['progress'] >= 70 else "#dc3545"
            st.markdown(f"""
                <div class="goal-progress-card">
                    <div class="goal-name">{goal['name']}</div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {goal['progress']}%; background-color: {color}"></div>
                    </div>
                    <div class="goal-details">{goal['progress']}% to {goal['target']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 💡 Insights & Recommendations")
        
        insights = [
            {"title": "Optimize Staffing", "insight": "Add 1 associate during 2-4 PM peak hours", "impact": "High", "icon": "👥"},
            {"title": "Inventory Alert", "insight": "Reorder designer jeans before weekend rush", "impact": "High", "icon": "📦"},
            {"title": "Promotion Opportunity", "insight": "Electronics trending +45% - extend promotion", "impact": "Medium", "icon": "📈"},
            {"title": "Training Need", "insight": "Customer service scores dipped in Men's Fashion", "impact": "Medium", "icon": "📚"}
        ]
        
        for insight in insights:
            impact_colors = {"High": "#dc3545", "Medium": "#ffc107", "Low": "#28a745"}
            st.markdown(f"""
                <div class="insight-card">
                    <div class="insight-header">
                        <span class="insight-icon">{insight['icon']}</span>
                        <span class="insight-title">{insight['title']}</span>
                        <span class="insight-impact" style="background-color: {impact_colors[insight['impact']]}">
                            {insight['impact']}
                        </span>
                    </div>
                    <div class="insight-text">{insight['insight']}</div>
                </div>
            """, unsafe_allow_html=True)

def show_floating_chat_window():
    """Legacy function - now redirects to modal implementation."""
    # This function is kept for backward compatibility
    # but the actual implementation is now in show_persistent_chat
    pass

# Legacy functions for backward compatibility (simplified versions)
def show_kpi_dashboard():
    """Legacy function - redirects to summary."""
    show_kpi_summary()

def show_notifications():
    """Legacy function - redirects to modal."""
    show_notifications_modal()

def show_inventory_status():
    """Legacy function - redirects to summary."""
    show_inventory_summary()

def show_homepage():
    """Main homepage function that routes to appropriate view based on user role."""
    # Get user role from session state
    user_role = st.session_state.get("user_role", "store_associate")
    
    # Get employee name and store name (keep full name including BrickMart)
    employee_name = st.session_state.config["employees"][st.session_state.user_role]["name"]
    store_name = st.session_state.store_name
    
    # Add chat modal setup
    chat_notifications = st.session_state.get("chat_notifications", 0)
    
    # Create the modal first
    chat_modal = modal.Modal(
        title="🤖 AI Assistant",
        key="homepage_chat_modal",
        max_width=700,
        padding=20
    )
    
    # Page header with integrated store info and chat button
    col1, col2 = st.columns([8, 2])
    
    with col1:
        # Enhanced title with company and location
        # Extract location from store name (remove "BrickMart" prefix if present)
        if store_name.startswith("BrickMart "):
            location = store_name.replace("BrickMart ", "").strip()
        else:
            location = store_name
        
        st.title(f"🏪 BrickMart - {location}")
        
        # Integrated store info bar - blends with header
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.now().strftime("%A, %B %d")
        
        # Get actual store data from database
        stores_df = get_stores()
        
        # Find current store data
        current_store_data = None
        if not stores_df.empty:
            # Find the store that matches the current store name
            matching_stores = stores_df[stores_df['name'] == store_name]
            if not matching_stores.empty:
                current_store_data = matching_stores.iloc[0]
        
        # Build store info from database or use fallback
        if current_store_data is not None:
            # Build complete address from database fields
            full_address = f"{current_store_data['address']}, {current_store_data['city']}, {current_store_data['state']} {current_store_data['zip_code']}"
            store_phone = current_store_data['phone']
            
            # Determine hours based on is_24_hours flag
            if current_store_data.get('is_24_hours', False):
                store_hours = "24/7"
            else:
                store_hours = "8:00 AM - 9:00 PM"  # Default hours
        else:
            # Fallback data if store not found in database
            full_address = "123 Main Street, San Francisco, CA 94102"
            store_phone = "(555) 123-4567"
            store_hours = "8:00 AM - 9:00 PM"
        
        store_info = {
            "address": full_address,
            "phone": store_phone,
            "hours": store_hours,
            "weather": "72°F ☀️"  # Weather remains mock for now
        }
        
        # Create a seamless info bar under the title
        st.markdown(f"""
            <div style="
                margin-top: -10px;
                margin-bottom: 15px;
                padding: 8px 0px;
                border-bottom: 1px solid #e9ecef;
                color: #6c757d;
                font-size: 14px;
            ">
                <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
                    <div style="font-weight: 600; color: #495057;">
                        <strong>Welcome back, {employee_name}!</strong>
                    </div>
                    <div style="display: flex; align-items: center; gap: 15px; font-size: 13px;">
                        <span><strong>🕐 {current_time}</strong> • {current_date}</span>
                        <span>🌤️ {store_info['weather']}</span>
                        <span>📍 {store_info['address']}</span>
                        <span>⏰ {store_info['hours']}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Add some spacing to align with title
        st.markdown("<br>", unsafe_allow_html=True)
        # Chat button with notification badge
        if chat_notifications > 0:
            button_text = f"💬 AI Assistant ({chat_notifications})"
        else:
            button_text = "💬 AI Assistant"
        
        if st.button(button_text, key="header_chat_btn", type="primary", use_container_width=True):
            st.session_state.chat_notifications = 0
            chat_modal.open()
    
    # Modal content
    if chat_modal.is_open():
        with chat_modal.container():
            # Get chat config with fallback
            chat_config = st.session_state.get("config", {}).get("chat", {
                "placeholder": "How can I help you today?",
                "max_tokens": 1000,
                "temperature": 0.7
            })
            
            # Show the chat container
            show_chat_container(chat_config)
    
    # Show appropriate homepage content based on user role
    if user_role == "store_manager":
        # Show new tab-based manager homepage
        show_manager_homepage()
    else:
        # Show new tab-based associate homepage
        show_associate_homepage() 