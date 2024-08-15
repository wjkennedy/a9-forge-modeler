# Atlassian Forge Quota Management App

## Overview

The Atlassian Forge Quota Management App is an interactive tool designed to help developers understand and manage the various quotas and limits associated with developing apps on the Atlassian Forge platform. This tool provides a comprehensive way to simulate different usage scenarios and visualize their impact on the platform's quotas, helping developers optimize their app's performance and avoid issues related to exceeding platform limits.

## Why This Tool is Relevant

As the Atlassian Forge platform grows, it becomes increasingly important for developers to manage resources efficiently. Atlassian imposes various quotas and limits to ensure stability and fair usage across the platform. These include limits on Function as a Service (FaaS) invocations, storage usage, resource updates, and more.

Exceeding these quotas can result in degraded app performance, unexpected errors, or even temporary suspension of the app. This tool helps developers by providing:

- **Visualization**: Graphs and plots that show how current usage compares to the imposed limits.
- **Optimization**: Suggestions for optimizing app performance based on the available quotas.
- **Scenario Modeling**: The ability to model different usage scenarios and see their impact on the quotas.

## Features

- **Multipage Navigation**: Easily navigate through different sections of the app to explore various quotas and limits.
- **Interactive Simulations**: Adjust parameters like the number of seats, invocations per seat, and more to see real-time changes in usage.
- **Comprehensive Summary**: View all relevant graphs and usage statistics on a single summary page.

## Installation

To install and run the app locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/forge-quota-management-app.git
    cd forge-quota-management-app
    ```

2. **Install Dependencies:**

    Ensure you have Python 3.7+ installed. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the App:**

    Launch the Streamlit app with the following command:

    ```bash
    streamlit run Home.py
    ```

4. **Access the App:**

    Open your web browser and navigate to `http://localhost:8501` to access the app.

## Usage

- **Home Page**: Start here to get an overview of the app and navigate to different sections.
- **Summary Page**: View a consolidated summary of all the graphs and usage metrics in one place.
- **Quota Sections**: Each section corresponds to a specific type of quota or limit, allowing you to drill down into details and optimize your app's performance accordingly.

## Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

