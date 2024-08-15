import streamlit as st
import matplotlib.pyplot as plt

st.title("Resource Update Quotas")

# Example Inputs
uploads_per_week = st.slider('Number of File Uploads per Week', min_value=1, max_value=1000, value=50)
file_size_per_upload = st.slider('Average File Size per Upload (MB)', min_value=1, max_value=100, value=5)

# Calculation Functions
def calculate_resource_updates(uploads_per_week, file_size_per_upload):
    total_upload_size = uploads_per_week * file_size_per_upload
    return uploads_per_week, total_upload_size

# Perform Calculations
total_uploads, total_upload_size = calculate_resource_updates(uploads_per_week, file_size_per_upload)

# Display Results
st.subheader('Estimated Weekly Resource Updates')
st.write(f"Total Uploads: {total_uploads}")
st.write(f"Total Upload Size: {total_upload_size} MB")

# Plot
categories = ['File Uploads', 'Total Size (MB)']
current_usage = [total_uploads, total_upload_size]
quotas = [500, 150]  # Example quota values for uploads and size

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Resource Update Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)
