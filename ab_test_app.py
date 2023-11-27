# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# !pip install streamlit pandas scipy

# ab_test_app.py
import streamlit as st
import pandas as pd
from scipy import stats

# Function to perform A/B test analysis
def perform_ab_test(data, group_col, metric_col):
    group_a = data[data[group_col] == 'A'][metric_col]
    group_b = data[data[group_col] == 'B'][metric_col]

    # Perform t-test for independent samples
    t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)

    return t_stat, p_value

# Streamlit app
def main():
    st.title('A/B Test Analysis')

    # File upload
    st.sidebar.header('Upload CSV File')
    uploaded_file = st.sidebar.file_uploader("Upload your A/B test data (.csv file)", type=['csv'])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.subheader('Uploaded Data')
        st.write(data)

        # Select columns for analysis
        st.sidebar.subheader('Select Columns')
        group_col = st.sidebar.selectbox('Select Group Column', data.columns)
        metric_col = st.sidebar.selectbox('Select Metric Column', data.columns)

        # Perform analysis if columns are selected
        if st.sidebar.button('Perform A/B Test'):
            try:
                t_stat, p_value = perform_ab_test(data, group_col, metric_col)
                st.write(f"t-statistic: {t_stat}")
                st.write(f"p-value: {p_value}")

                # Interpretation of the results
                alpha = 0.05
                if p_value < alpha:
                    st.write("Statistically significant difference detected between groups A and B!")
                else:
                    st.write("No statistically significant difference detected between groups A and B.")
            except Exception as e:
                st.error(f"Error: {e}")

# Run the app
if __name__ == '__main__':
    main()

#streamlit run ab_test_app.py
#streamlit run /opt/conda/lib/python3.7/site-packages/ipykernel_launcher.py

# -






