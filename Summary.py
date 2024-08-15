import streamlit as st
import matplotlib.pyplot as plt

st.title("Summary of Quotas and Limits")

# Usage-based Quotas
st.subheader("Usage-based Quotas")
seats = 100
invocations_per_seat = 50
avg_invocation_time = 500
total_invocations = seats * invocations_per_seat
total_runtime = total_invocations * (avg_invocation_time / 1000) / 60  # minutes
total_data = total_invocations * (32 / 1000)  # MB

categories = ['Invocations', 'Runtime (min)', 'Data (MB)']
current_usage = [total_invocations, total_runtime, total_data]
quotas = [5050000, 20200, 99000]  # Example quota values

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Usage-based Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)

# Installation Quotas
st.subheader("Installation Quotas")
installations = 10
seats_per_installation = 100
total_seats = installations * seats_per_installation

categories = ['Installations', 'Seats']
current_usage = [installations, total_seats]
quotas = [10000, 1000000]  # Example quota values

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Installation Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)

# Function as a Service Quotas
st.subheader("Function as a Service Quotas")
fig, ax = plt.subplots()
categories = ['Invocations', 'Runtime (min)']
current_usage = [total_invocations, total_runtime]
quotas = [5050000, 20200]  # Example quota values

ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('FaaS Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)

# Resource Update Quotas
st.subheader("Resource Update Quotas")
uploads_per_week = 50
file_size_per_upload = 5
total_upload_size = uploads_per_week * file_size_per_upload

categories = ['File Uploads', 'Total Size (MB)']
current_usage = [uploads_per_week, total_upload_size]
quotas = [500, 150]  # Example quota values for uploads and size

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Resource Update Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)

# Storage Quotas
st.subheader("Storage Quotas")
storage_per_seat = 12
total_storage = seats * storage_per_seat

categories = ['Total Storage (MB)']
current_usage = [total_storage]
quotas = [1200 * 100]  # Example quota value (100 installations, 1200MB per installation)

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Storage Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)
