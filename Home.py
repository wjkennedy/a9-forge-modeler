import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    [
        "Home",
        "Summary",
        "Usage-based Quotas",
        "Installation Quotas",
        "Function as a Service Quotas",
        "Resource Update Quotas",
        "Storage Quotas",
        "Platform Limits",
        "Invocation Limits",
        "Resource Limits",
        "Storage Limits",
        "Async Events Limits",
        "Apps Exceeding Quotas or Limits",
        "Suspended Apps",
    ]
)

# Navigation logic
if page == "Home":
    st.title("Atlassian Forge Quota Management App")
    st.markdown("""
    Welcome to the Atlassian Forge Quota Management App. This app helps you understand and manage the various quotas and limits associated with developing apps on the Forge platform.

    Use the sidebar to navigate through the different sections based on the type of quota or limit you want to explore.
    """)
    st.image("https://a9group.net/a9logo.png", use_column_width=True)

elif page == "Summary":
    exec(open("Summary.py").read())

elif page == "Usage-based Quotas":
    exec(open("Usage_based_quotas.py").read())
    
elif page == "Installation Quotas":
    exec(open("Installation_quotas.py").read())
    
elif page == "Function as a Service Quotas":
    exec(open("Function_as_a_Service_quotas.py").read())
    
elif page == "Resource Update Quotas":
    exec(open("Resource_update_quotas.py").read())
    
elif page == "Storage Quotas":
    exec(open("Storage_quotas.py").read())
    
elif page == "Platform Limits":
    exec(open("Platform_limits.py").read())
    
elif page == "Invocation Limits":
    exec(open("Invocation_limits.py").read())
    
elif page == "Resource Limits":
    exec(open("Resource_limits.py").read())
    
elif page == "Storage Limits":
    exec(open("Storage_limits.py").read())
    
elif page == "Async Events Limits":
    exec(open("Async_events_limits.py").read())
    
elif page == "Apps Exceeding Quotas or Limits":
    exec(open("Apps_exceeding_quotas_or_limits.py").read())
    
elif page == "Suspended Apps":
    exec(open("Suspended_apps.py").read())
