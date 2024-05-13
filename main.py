import streamlit as st
import pandas as pd
from joblib import load

model = load('employee_satisfaction_model.joblib')

st.title('Employee Satisfaction Prediction')

st.sidebar.header('Input Employee Information')

last_evaluation = st.sidebar.number_input('Last Evaluation', min_value=0.0, max_value=1.0, value=0.70, step=0.01)
number_project = st.sidebar.number_input('Number of Projects', min_value=1, max_value=10, value=3)
average_montly_hours = st.sidebar.number_input('Average Monthly Hours', min_value=80, max_value=320, value=200)
time_spend_company = st.sidebar.number_input('Time Spent at Company (years)', min_value=1, max_value=20, value=3)
work_accident = st.sidebar.selectbox('Work Accident', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
promotion_last_5years = st.sidebar.selectbox('Promotion in Last 5 Years', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

unique_departments = ['sales', 'accounting', 'hr', 'technical', 'support', 'management', 'IT', 'product_mng', 'marketing']
unique_salary = ['low', 'medium', 'high']
department = st.sidebar.selectbox('Department', unique_departments)
salary = st.sidebar.selectbox('Salary Level', unique_salary)


if st.sidebar.button('Predict Satisfaction'):
    new_employee = pd.DataFrame({
        'last_evaluation': [last_evaluation],
        'number_project': [number_project],
        'average_montly_hours': [average_montly_hours],
        'time_spend_company': [time_spend_company],
        'Work_accident': [work_accident],
        'left': [0],
        'promotion_last_5years': [promotion_last_5years],
        'Department': [department],
        'salary': [salary]
    })

    prediction = model.predict(new_employee)
    st.success(f'Predicted Satisfaction Level: {prediction[0]:.2f}')
    

st.write("On the left side, for the employee's satisfaction level you wish to predict, input the requested information and then hit the predict buttion at the end.")
st.write("\n\n\n\n\n\n\n")   
st.write("Click the button below to lead you to the tableau dashboard with interactive visualizations. Click the department you wish to learn more about on the bar chart and you will see related information through the other charts.")    
url = "https://public.tableau.com/views/SatisfactionLevel_17154527849660/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link"
st.markdown(f'<a href="{url}" target="_blank"><button style="color: white; background-color: #FF4B4B; border: none; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px; border-radius: 10px; cursor: pointer;">Visualizations</button></a>', unsafe_allow_html=True)
