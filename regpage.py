import streamlit as st
import joblib

#model = joblib.load("lg.joblib.diab")

st.title('Diabetes Classification Prediction')
st.write("Follow the instructions to get a prediction")

options = ["General Health is Excellent", "General Health is Very Good", "General Health is Good", " General Health is Fair", "General Health is Poor"]
question1 = st.selectbox("Choose the option that best describes your general health:", options)
question1_dict = {"General Health is Excellent": 1.0, "General Health is Very Good": 2.0, "General Health is Good": 3.0, " General Health is Fair": 4.0, "General Health is Poor": 5.0}
question1_ans = question1_dict[question1]

question2 = st.number_input("Enter the value that represents how many of the past 30 days your physical health wasn't good from 0 to 30")
question2_ans = question2.astype("float")

question3 = st.number_input("Enter the value that represents how many of the past 30 days your mental health wans't good from 0 to 30")
question3_ans = question3.astype("float")

question4_options = ["Yes", "No"]
question4 = st.selectbox("If you have any form of insurance, select Yes. If not, select NO", question4_options)
question4_dict = {"Yes": 1.0, "No": 0.0}
question4_ans = question4_dict[question4]

question5_options = question4_options 
question5 = st.selectbox("If you have had physical activiity or excercise in the past 30 days other than your job, select Yes. If not, select No", question5_options)
question5_dict = question4_dict
question5_ans = question5_dict[questions]

question6_options = ["150+", "1-149", "0"]
question6 = st.selectbox("Select the option that corresponds to the number of minutes of physical acitivity you have had in the past week (in minutes). 150+ mean more than 150 minutes.", question6_options)









