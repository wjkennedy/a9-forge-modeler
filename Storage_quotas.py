import streamlit as st
import matplotlib.pyplot as plt

st.title("Storage Quotas")

# Example Inputs
seats = st.number_input('Number of Seats', min_value=10, max_value=10000, step=10, value=100)
storage_per_seat = st.slider('Storage per Seat (MB)', min_value=1, max_value=100, value=12)

# Calculation Functions
def calculate_storage_quota(seats, storage_per_seat):
    total_storage = seats * storage_per_seat
    return total_storage

# Perform Calculations
total_storage = calculate_storage_quota(seats, storage_per_seat)

# Display Results
st.subheader('Estimated Total Storage Usage')
st.write(f"Total Storage: {total_storage} MB")

# Plot
categories = ['Total Storage (MB)']
current_usage = [total_storage]
quotas = [1200 * 100]  # Example quota value (100 installations, 1200MB per installation)

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Storage Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)
