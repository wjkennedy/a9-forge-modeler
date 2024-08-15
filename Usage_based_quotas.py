import streamlit as st
import matplotlib.pyplot as plt

st.title("Usage-based Quotas")

# Example Inputs
seats = st.number_input('Number of Seats', min_value=10, max_value=10000, step=10, value=100)
invocations_per_seat = st.slider('FaaS Invocations per Seat (weekly)', min_value=10, max_value=200, value=50)
avg_invocation_time = st.slider('Average Invocation Time (ms)', min_value=100, max_value=2000, value=500)
data_per_invocation = st.slider('Data Returned per Invocation (KB)', min_value=1, max_value=100, value=32)

# Calculation Functions
def calculate_faas_usage(seats, invocations_per_seat, avg_invocation_time, data_per_invocation):
    total_invocations = seats * invocations_per_seat
    total_runtime = total_invocations * (avg_invocation_time / 1000) / 60  # minutes
    total_data = total_invocations * (data_per_invocation / 1000)  # MB
    return total_invocations, total_runtime, total_data

# Perform Calculations
total_invocations, total_runtime, total_data = calculate_faas_usage(seats, invocations_per_seat, avg_invocation_time, data_per_invocation)

# Display Results
st.subheader('Estimated Weekly FaaS Usage')
st.write(f"Total Invocations: {total_invocations:,}")
st.write(f"Total Runtime: {total_runtime:.2f} minutes")
st.write(f"Total Data Returned: {total_data:.2f} MB")

# Plot
categories = ['Invocations', 'Runtime (min)', 'Data (MB)']
current_usage = [total_invocations, total_runtime, total_data]
quotas = [5050000, 20200, 99000]  # Example quota values

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Usage vs Quota')
ax.legend()
st.pyplot(fig)
