import streamlit as st

# Page config
st.set_page_config(page_title="Dashboard Viewer", layout="wide")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        .title-bar {
            background-color: #0e1117;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        .title-bar h1 {
            color: white;
            margin: 0;
        }
        .nav-tabs {
            display: flex;
            gap: 2rem;
            margin-bottom: 1rem;
        }
        .nav-tabs button {
            background-color: #f0f2f6;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        .filters-section {
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
        }
        .view-options {
            position: absolute;
            left: 1rem;
            top: 6rem;
            font-size: 0.9rem;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title Bar ---
st.markdown("""
    <div class="title-bar">
        <h1>📊 Dashboard Viewer</h1>
    </div>
""", unsafe_allow_html=True)

# --- Navigation Tabs ---
st.markdown("""
    <div class="nav-tabs">
        <button>Previous Dashboard</button>
        <button>Current Dashboard</button>
        <button>Compare with Previous One</button>
    </div>
""", unsafe_allow_html=True)

# --- View Options (left side) ---
st.markdown("""
    <div class="view-options">
        ➤ Tabular View<br>
        ➤ Dashboard View (default one)
    </div>
""", unsafe_allow_html=True)

# --- Filters Section ---
with st.container():
    st.markdown("### 🔍 Filters")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Select Category", ["All", "Sales", "Marketing", "Finance"])
    with col2:
        st.date_input("Start Date")
    with col3:
        st.date_input("End Date")

# --- Placeholder for Graph or Backend Output ---
st.info("📌 Graph or data visualization will be rendered here by backend processing.")
