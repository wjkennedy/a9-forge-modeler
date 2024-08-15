import streamlit as st
import matplotlib.pyplot as plt

st.title("Invocation Limits")

# Example Inputs
invocations = st.number_input('Number of Invocations in 25-Second Window', min_value=1, max_value=1000, value=100)

# Limits
max_invocations = 500

# Display Results
st.subheader('Invocation Limits')
if invocations > max_invocations:
    st.write(f"Warning: You are exceeding the invocation limit! ({invocations} invocations > {max_invocations} limit)")
else:
    st.write(f"Invocations: {invocations} (within the limit of {max_invocations})")

# Plot
categories = ['Invocations']
current_usage = [invocations]
limits = [max_invocations]

fig, ax = plt.subplots()
ax.barh(categories, limits, color='lightgrey', label='Limit')
ax.barh(categories, current_usage, color='orange', label='Your Usage')
ax.set_title('Invocation Limits')
ax.legend()
st.pyplot(fig)
