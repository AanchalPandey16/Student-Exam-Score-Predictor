import streamlit as st # type: ignore
import numpy as np
import joblib

model = joblib.load('model.pkl')

st.title("Student Exam Score Predictor")

gender = st.selectbox('Select Gender:', ['female', 'male'])
gender = 1 if gender == 'male' else 0

edu_levels = {
    'high school': 0,
    'some college': 1,
    'associate\'s degree': 2,
    'bachelor\'s degree': 3,
    'master\'s degree': 4,
    'some high school': 5
}
edu_label = st.selectbox('Parental Level of Education:', list(edu_levels.keys()))
parent_edu = edu_levels[edu_label]

lunch = st.selectbox('Lunch Type:', ['free/reduced', 'standard'])
lunch = 1 if lunch == 'standard' else 0

prep = st.selectbox('Test Preparation Course:', ['none', 'completed'])
prep = 1 if prep == 'completed' else 0


if st.button('Predict'):
    input_data = np.array([[gender, parent_edu, lunch, prep]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Exam Score: **{prediction[0]:.2f}**")
