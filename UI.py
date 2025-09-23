import streamlit as st
import plotly.express as px

# Sidebar
st.sidebar.title("Navigation")
view = st.sidebar.radio(
    "Select View",
    ("Tabular View", "Dashboard View (default one)"),
    index=1
)

# Main area
st.title("Dashboard")

# Tabs at the top
tab1, tab2, tab3 = st.tabs(["previous dashboard", "current dashboard", "compare with the previous one"])

with tab1:
    st.write("This is the previous dashboard view.")

with tab2:
    st.write("This is the current dashboard view.")

with tab3:
    st.write("This is the comparison with the previous dashboard.")

# Horizontal filter section
st.markdown("---")
st.markdown("### Filters")
st.markdown("---")

# Placeholder pie chart
pie_data = {
    "Category": ["A", "B", "C", "D"],
    "Value": [30, 20, 25, 25]
}
fig = px.pie(pie_data, names="Category", values="Value", title="Sample Pie Chart")
st.plotly_chart(fig, use_container_width=True)
