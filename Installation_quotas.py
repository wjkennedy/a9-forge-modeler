import streamlit as st
import matplotlib.pyplot as plt

st.title("Installation Quotas")

# Example Inputs
installations = st.number_input('Number of Installations', min_value=1, max_value=10000, step=1, value=10)
seats_per_installation = st.slider('Average Seats per Installation', min_value=1, max_value=1000, value=100)

# Calculation Functions
def calculate_installation_quotas(installations, seats_per_installation):
    total_seats = installations * seats_per_installation
    return total_seats

# Perform Calculations
total_seats = calculate_installation_quotas(installations, seats_per_installation)

# Display Results
st.subheader('Total Seats Across Installations')
st.write(f"Total Seats: {total_seats:,}")

# Plot
categories = ['Installations', 'Seats']
current_usage = [installations, total_seats]
quotas = [10000, 1000000]  # Example quota values

fig, ax = plt.subplots()
ax.plot(categories, quotas, 'go--', label='Quota')
ax.plot(categories, current_usage, 'ro', label='Current Usage')
ax.set_title('Installation Quotas vs Current Usage')
ax.legend()
st.pyplot(fig)
