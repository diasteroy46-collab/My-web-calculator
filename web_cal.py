import streamlit as st

# This sets up the title of your webpage
st.title("Thekxdd's Web Calculator")

# Create a simple layout with two number input boxes
num1 = st.number_input("Enter your first number", value=0.0)
num2 = st.number_input("Enter your second number", value=0.0)

# Create a dropdown menu for math operations
operation = st.selectbox("Choose what to do:", ["Add", "Subtract", "Multiply", "Divide"])

# This button performs the calculation when clicked
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        # We check for zero to avoid a "division by zero" error
        result = num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"
    
    # This displays the final answer in a nice green box
    st.success(f"The result is: {result}")