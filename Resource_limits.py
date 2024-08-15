import streamlit as st

st.title("Resource Limits")

# Information
st.markdown("""
Resource limits pertain to specific boundaries on the resources your app can consume. These include:

- **Memory:** Maximum memory per invocation.
- **Log size:** Maximum size of all log line data generated per invocation.
- **Network requests:** Maximum number of network requests per invocation.

Understanding these limits helps in optimizing your app to run efficiently within the Forge environment.
""")
