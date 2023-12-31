import streamlit as st
import pandas as pd
from scipy.stats import ttest_ind

# Function to perform t-test
def perform_t_test(group_a_data, group_b_data):
    t_statistic, p_value = ttest_ind(group_a_data, group_b_data)
    return t_statistic, p_value

# Streamlit app
def main():
    st.title("A/B Test Evaluation with T-Test")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(df)

        test_group_a = st.sidebar.selectbox("Select Test Group A column", df.columns)
        test_group_b = st.sidebar.selectbox("Select Test Group B column", df.columns)
        metric = st.sidebar.selectbox("Select Metric to Evaluate", df.columns)

        if st.button("Run T-Test"):
            group_a_data = df[test_group_a].values
            group_b_data = df[test_group_b].values

            t_statistic, p_value = perform_t_test(group_a_data, group_b_data)

            st.write(f"T-Statistic: {t_statistic}")
            st.write(f"P-Value: {p_value}")

            if p_value < 0.05:
                st.write("Statistically significant difference observed between the groups.")
            else:
                st.write("No statistically significant difference observed.")

if __name__ == "__main__":
    main()



# import streamlit as st
# import pandas as pd
# from scipy.stats import ttest_ind

# # Function to perform t-test
# def perform_t_test(group_a, group_b, metric):
#     # Perform independent t-test
#     t_stat, p_value = ttest_ind(group_a[metric], group_b[metric])
#     return t_stat, p_value

# # Function to load CSV file
# def load_data(file):
#     data = pd.read_csv(file)
#     return data

# # Function to display A/B test results
# def display_results(group_a, group_b, metric, p_value):
#     st.write("### A/B Test Results:")
#     st.write(f"- **Group A ({group_a_name}):** Mean {metric}: {group_a[metric].mean()}")
#     st.write(f"- **Group B ({group_b_name}):** Mean {metric}: {group_b[metric].mean()}")
#     st.write(f"- **p-value:** {p_value}")

# # Streamlit app
# def main():
#     st.title('A/B Test Evaluation App')

#     # Upload CSV file
#     st.write("### Upload A/B Test Data")
#     file = st.file_uploader("Upload CSV", type=["csv"])

#     if file is not None:
#         data = load_data(file)
#         st.write("### A/B Test Data Preview")
        st.write(data.head())

        # Select test groups and metrics
        st.write("### Configure A/B Test")
        test_groups = data['group'].unique()
        test_group_a = st.selectbox("Select Group A", test_groups)
        test_group_b = st.selectbox("Select Group B", test_groups)
        metric_to_evaluate = st.selectbox("Select Metric", data.columns)

        group_a_data = data[data['group'] == test_group_a]
        group_b_data = data[data['group'] == test_group_b]

        # Perform t-test and display results
        if st.button("Run A/B Test"):
            t_statistic, p_value = perform_t_test(group_a_data, group_b_data, metric_to_evaluate)
            group_a_name = group_a_data['name'].unique()[0] if 'name' in group_a_data.columns else test_group_a
            group_b_name = group_b_data['name'].unique()[0] if 'name' in group_b_data.columns else test_group_b
            display_results(group_a_data, group_b_data, metric_to_evaluate, p_value)

if __name__ == "__main__":
    main() 
