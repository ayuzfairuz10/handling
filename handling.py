import streamlit as st

st.title("Division with Error Handling")


col1, col2 = st.columns(2)
with col1:
    num1 = st.text_input("First number (dividend):")
with col2:
    num2 = st.text_input("Second number (divisor):")

if st.button("Calculate Division"):
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 / n2
        st.success(f"Result: {n1} ÷ {n2} = {result}")
    except ValueError:
        st.error("Error: Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        st.error("Error: Cannot divide by zero!")