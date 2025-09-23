import streamlit as st

# Page configuration
st.set_page_config(page_title="Dashboard Viewer", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main-container {
            display: flex;
            flex-direction: row;
        }
        .sidebar-custom {
            width: 220px;
            background-color: #f0f2f6;
            padding: 1rem;
            height: 100vh;
            border-right: 1px solid #ddd;
        }
        .sidebar-custom h3 {
            margin-top: 0;
        }
        .menu-icon {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .nav-link {
            margin: 0.5rem 0;
            font-weight: bold;
            color: #333;
        }
        .content-area {
            flex: 1;
            padding: 1rem 2rem;
        }
        .title-bar {
            background-color: #0e1117;
            color: white;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        .button-row {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        .filters-row {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Layout ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.markdown("""
    <div class="sidebar-custom">
        <div class="menu-icon">☰</div>
        <div class="nav-link">Dashboard View (default one)</div>
        <div class="nav-link">Tabular View</div>
    </div>
""", unsafe_allow_html=True)

# --- Main Content Area ---
st.markdown('<div class="content-area">', unsafe_allow_html=True)

# Title Bar
st.markdown('<div class="title-bar"><h2>📊 Dashboard Viewer</h2></div>', unsafe_allow_html=True)

# Navigation Buttons
st.markdown("""
    <div class="button-row">
        <button>Previous Dashboard</button>
        <button>Current Dashboard</button>
        <button>Compare with Previous One</button>
    </div>
""", unsafe_allow_html=True)

# Filters Section
st.markdown('<div class="filters-row">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Filter 1")
with col2:
    st.text_input("Filter 2")
with col3:
    st.text_input("Filter 3")
st.markdown('</div>', unsafe_allow_html=True)

# Placeholder for backend dashboard
st.info("📌 Space for dashboard that will come from backend.")

# Close main content div
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
