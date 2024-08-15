import streamlit as st

st.title("Storage Limits")

# Information
st.markdown("""
Storage limits refer to the constraints on how much data your app can store using Forge's storage API. Key limits include:

- **Total storage capacity per seat:** Maximum storage allocated per seat.
- **Read and write capacity:** Amount of data that can be transferred in or out of the Storage API each week.

Ensure that your app's data storage strategy adheres to these limits to avoid performance issues or data loss.
""")
