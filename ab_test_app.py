!pip install streamlit
!pip install python
!pip install pandas
!pip install scipy.stats


import streamlit as st
import pandas as pd
from scipy.stats import ttest_ind

# Function to perform t-test
def perform_t_test(group_a, group_b, metric):
    # Perform independent t-test
    t_stat, p_value = ttest_ind(group_a[metric], group_b[metric])
    return t_stat, p_value

# Function to load CSV file
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to display A/B test results
def display_results(group_a, group_b, metric, p_value):
    st.write("### A/B Test Results:")
    st.write(f"- **Group A ({group_a['name'].unique()[0]}):** Mean {metric}: {group_a[metric].mean()}")
    st.write(f"- **Group B ({group_b['name'].unique()[0]}):** Mean {metric}: {group_b[metric].mean()}")
    st.write(f"- **p-value:** {p_value}")

# Streamlit app
def main():
    st.title('A/B Test Evaluation App')

    # Upload CSV file
    st.write("### Upload A/B Test Data")
    file = st.file_uploader("Upload CSV", type=["csv"])

    if file is not None:
        data = load_data(file)
        st.write("### A/B Test Data Preview")
        st.write(data.head())

        # Select test groups and metrics
        st.write("### Configure A/B Test")
        test_group_a = st.selectbox("Select Group A", data['group'].unique())
        test_group_b = st.selectbox("Select Group B", data['group'].unique())
        metric_to_evaluate = st.selectbox("Select Metric", data.columns)

        group_a_data = data[data['group'] == test_group_a]
        group_b_data = data[data['group'] == test_group_b]

        # Perform t-test and display results
        if st.button("Run A/B Test"):
            t_statistic, p_value = perform_t_test(group_a_data, group_b_data, metric_to_evaluate)
            display_results(group_a_data, group_b_data, metric_to_evaluate, p_value)

if __name__ == "__main__":
    main()
