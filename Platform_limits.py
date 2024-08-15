import streamlit as st

st.title("Platform Limits")

# Information
st.markdown("""
Platform limits refer to specific boundaries set by Atlassian for various operations, including function invocations, memory usage, and network requests. Exceeding these limits can result in errors or degraded performance of your app.

Here are some key platform limits:

- **Invocation rate limit:** Maximum number of invocations per 25-second sliding window.
- **Runtime limit:** Maximum runtime before the app is stopped.
- **Memory limit:** Available memory per invocation.
- **Network requests:** Number of network requests per invocation.

Ensure that your app operates within these limits to avoid disruptions.
""")
