import streamlit as st
import matplotlib.pyplot as plt

st.title("Function as a Service Quotas")

# Example Inputs
seats = st.number_input('Number of Seats', min_value=10, max_value=10000, step=10, value=100)
invocations_per_seat = st.slider('FaaS Invocations per Seat (weekly)', min_value=10, max_value=200, value=50)
avg_invocation_time = st.slider('Average Invocation Time (ms)', min_value=100, max_value=2000, value=500)

# Calculation Functions
def calculate_faas_usage(seats, invocations_per_seat, avg_invocation_time):
    total_invocations = seats * invocations_per_seat
    total_runtime = total_invocations * (avg_invocation_time / 1000) / 60  # minutes
    return total_invocations, total_runtime

# Perform Calculations
total_invocations, total_runtime = calculate_faas_usage(seats, invocations_per_seat, avg_invocation_time)

# Display Results
st.subheader('Estimated Weekly FaaS Usage')
st.write(f"Total Invocations: {total_invocations:,}")
st.write(f"Total Runtime: {total_runtime:.2f} minutes")

# Plot
categories = ['Invocations', 'Runtime (min)']
current_usage = [total_invocations, total_runtime]
quotas = [5050000, 20200]  # Example quota values

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('FaaS Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)
