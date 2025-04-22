import streamlit as st
import requests

st.title("Calculator")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Select operation", ["add", "subtract", "multiply", "divide"])

# Button block
if st.button("Calculate"):
    try:
        response = requests.post("http://localhost:8000/calculate", json={
            "num1": num1,
            "num2": num2,
            "operation": operation
        })

        if response.status_code == 200:
            data = response.json()
            if "result" in data:
                st.success(f"Result: {data['result']}")
            else:
                st.error(data.get("error", "Unknown error"))
        else:
            st.error("Error from backend")
    except Exception as e:
        st.error(f"Request failed: {e}")
