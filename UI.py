import streamlit as st

# Streamlit UI setup
st.title("🔢 Square Numbers App")
st.write("Enter a list of numbers separated by commas, and we'll square each one for you!")

# Input from user
user_input = st.text_input("Enter numbers (comma-separated):", "1,2,3,4,5,6,7")

# Process input and display results
if user_input:
    try:
        # Convert input string to list of integers
        num_list = [int(x.strip()) for x in user_input.split(",")]
        squared_list = [i * i for i in num_list]

        # Display results
        st.subheader("✅ Squared Results")
        for original, squared in zip(num_list, squared_list):
            st.write(f"{original}² = {squared}")
    except ValueError:
        st.error("Please enter valid integers separated by commas.")