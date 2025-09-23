import streamlit as st

# Page configuration
st.set_page_config(page_title="Dashboard Viewer", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        .title-bar {
            background-color: #0e1117;
            color: white;
            padding: 1rem 2rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        .sidebar-custom {
            background-color: #f0f2f6;
            padding: 1.5rem 1rem;
            height: 100%;
            border-right: 1px solid #ddd;
            border-radius: 0.5rem;
        }
        .sidebar-custom h4 {
            margin-top: 0;
        }
        .nav-link {
            margin: 1rem 0;
            font-weight: bold;
            color: #333;
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

# --- Title Bar (Full Width) ---
st.markdown('<div class="title-bar"><h2>📊 Dashboard Viewer</h2></div>', unsafe_allow_html=True)

# --- Layout: Sidebar + Main Content ---
sidebar, main = st.columns([1, 5])

# --- Sidebar Navigation ---
with sidebar:
    st.markdown("""
        <div class="sidebar-custom">
            <div style="font-size: 1.5rem;">☰</div>
            <div class="nav-link">Dashboard View (default one)</div>
            <div class="nav-link">Tabular View</div>
        </div>
    """, unsafe_allow_html=True)

# --- Main Content Area ---
with main:
    # Navigation Buttons
    st.markdown("""
        <div class="button-row">
            <button>Previous Dashboard</button>
            <button>Current Dashboard</button>
            <button>Compare with Previous One</button>
        </div>
    """, unsafe_allow_html=True)

    # Filters Section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_input("Filter 1")
    with col2:
        st.text_input("Filter 2")
    with col3:
        st.text_input("Filter 3")

    # Placeholder for backend dashboard
    st.info("📌 Space for dashboard that will come from backend.")
