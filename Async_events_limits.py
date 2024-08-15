import streamlit as st

st.title("Async Events Limits")

# Information
st.markdown("""
Async events in Forge allow your app to handle tasks asynchronously, but there are limits to consider:

- **Event per request:** Maximum number of events pushed in a single request.
- **Event per minute:** Maximum number of events pushed in one minute.
- **Payload size:** Maximum combined payload size of events in a single request.

Staying within these limits ensures that your app can handle events efficiently without overwhelming the system.
""")
