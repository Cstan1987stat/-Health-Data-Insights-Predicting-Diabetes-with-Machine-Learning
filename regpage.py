import streamlit as st
import joblib
import pandas as pd

model = joblib.load("lg.joblib.diab")

st.title('Diabetes Classification Prediction')
st.write("Follow the instructions to get a prediction")

options = ["General Health is Excellent", "General Health is Very Good", "General Health is Good", " General Health is Fair", "General Health is Poor"]
question1 = st.selectbox("Choose the option that best describes your general health:", options)
question1_dict = {"General Health is Excellent": 1.0, "General Health is Very Good": 2.0, "General Health is Good": 3.0, " General Health is Fair": 4.0, "General Health is Poor": 5.0}
question1_ans = question1_dict[question1]

question2_ans = st.number_input("Enter the value that represents how many of the past 30 days your physical health wasn't good from 0 to 30")

question3_ans = st.number_input("Enter the value that represents how many of the past 30 days your mental health wans't good from 0 to 30")

question4_options = ["Yes", "No"]
question4 = st.selectbox("If you have any form of insurance, select Yes. If not, select NO", question4_options)
question4_dict = {"Yes": 1.0, "No": 0.0}
question4_ans = question4_dict[question4]

question5_options = question4_options 
question5 = st.selectbox("If you have had physical activiity or excercise in the past 30 days other than your job, select Yes. If not, select No", question5_options)
question5_dict = question4_dict
question5_ans = question5_dict[question5]

question6_options = ["150+", "1-149", "0"]
question6 = st.selectbox("Select the option that corresponds to the number of minutes of physical acitivity you have had in the past week (in minutes). 150+ mean more than 150 minutes.", question6_options)
question6_dict = {"150+": 1.0, "1-149": 2.0, "0": 3.0}
question6_ans = question6_dict[question6]

question7_options = question4_options
question7 = st.selectbox("If you meet muscle strengthening recommendations, select Yes. If you don't, select No", question7_options)
question7_dict = question4_dict
question7_ans = question7_dict[question7]

question8_options = ["No", "Yes"]
question8 = st.selectbox("Select the option that corresponds to whether you have been told you have high blood pressure", question8_options)
question8_dict = {"No": 1.0, "Yes": 0.0}
question8_ans = question8_dict[question8]

question9_options = question8_options 
question9 = st.selectbox("Select the option that corresponds to whether you have been told you have high cholesterol", question9_options)
question9_dict =  question8_dict
question9_ans = question9_dict[question9]

question10_options = question8_options 
question10 = st.selectbox("Select the option that corresponds to whether you have had a heart attack or have coronary heart disease", question10_options)
question10_dict =  question8_dict
question10_ans = question10_dict[question10]

question11_options = question8_options 
question11 = st.selectbox("Select the option that corresponds to whether you have been told you have asthma", question11_options)
question11_dict =  question8_dict
question11_ans = question11_dict[question11]

question12_options = question8_options 
question12 = st.selectbox("Select the option that corresponds to whether you have been told you have arthritis", question12_options)
question12_dict =  question8_dict
question12_ans = question12_dict[question12]

question13_options = ["Male","Female"]
question13 = st.selectbox("Select the sex you were at birth", question13_options)
question13_dict = {"Male": 1.0, "Female": 0.0}
question13_ans = question13_dict[question13]

question14_ans = st.number_input("Enter your age: (18-99)")

question15_ans = st.number_input("Enter your height in inches: (36-95)")

question16_ans = st.number_input("Enter your body mass index:")

question17_options = ["Didn't graduate High School", "Graduated High School", "Attended College or Technical School", "Graduated from College or Technical School"]
question17 = st.selectbox("Please select the option that corresponds to your education journey:", question17_options)
question17_dict = {"Didn't graduate High School": 1.0, "Graduated High School": 2.0, "Attended College or Technical School": 3.0, "Graduated from College or Technical School": 4.0}
question17_ans = question17_dict[question17]

question18_options = ["income < $15,000", "$15,000 < income < $25,000", "$25,000 < income < $35,000", "$35,000 < income < $50,000", "$50,000 < income < $100,000", "$100,000 < income < $200,000", "income > $200,000"]
question18 = st.selectbox("Please select the option that corresponds to total yearly income", question18_options)
question18_dict = {"income < $15,000": 1.0, "$15,000 < income < $25,000": 2.0, "$25,000 < income < $35,000": 3.0, "$35,000 < income < $50,000": 4.0, 
                   "$50,000 < income < $100,000": 5.0, "$100,000 < income < $200,000": 6.0, "income > $200,000": 7.0}
question18_ans = question18_dict[question18]

question19_options = ["Everyday smoker", "Smokes some days", "Former smoker", "Never smoked"]
question19 = st.selectbox("Please select the option that corresponds to any smoking you may or may not have done", question19_options)
question19_dict = {"Everyday smoker": 1.0, "Smokes some days": 2.0, "Former smoker": 3.0, "Never smoked": 4.0}
question19_ans = question19_dict[question19]

question20_options = ["Yes", "No"]
question20 = st.selectbox("Please select the options that corresponds to whether you've had at least one drink of alcohol in the past 30 days:", question20_options)
question20_dict = {"Yes": 1.0, "No": 0.0}
question20_ans = question20_dict[question20]

question21_options = ["No", "Yes"]
question21 = st.selectbox("Please select whether you are a binge drinker (5 or more drinks for me and 4 or more drinks for women on one occasion):", question21_options)
question21_dict = {"No": 1.0, "Yes": 0.0}
question21_ans = question21_dict[question21]

question22_options = ["Yes", "No"]
question22 = st.selectbox("Please select whether you are a heavy drinker (15 or more drinks for men in a week or 8 or more drinks for women in a week:", question22_options)
question22_dict = {"Yes": 0.0, "No": 1.0}
question22_ans = question22_dict[question22]

question23_options = ["Yes", "No"]
question23 = st.selectbox("Please select whether you have difficulty walking or climbing stairs:", question23_options)
question23_dict = {"Yes" : 1.0, "No" : 0.0}
question23_ans = question23_dict[question23]



question_answers = [question1_ans, question2_ans, question3_ans, question4_ans, question5_ans,
                    question6_ans, question7_ans, question8_ans, question9_ans, question10_ans,
                    question11_ans, question12_ans, question13_ans, question14_ans, question15_ans, 
                    question16_ans, question17_ans, question18_ans, question19_ans, question20_ans,
                    question21_ans, question22_ans, question23_ans
]

cols = ['general_health', 'physical_health_days', 'mental_health_days',
       'has_health_plan', 'meets_aerobic_guidelines',
       'physical_activity_150min', 'muscle_strengthening',
       'high_blood_pressure', 'high_cholesterol', 'heart_disease',
       'lifetime_asthma', 'arthritis', 'sex', 'age', 'height_inches', 'bmi',
       'education_level', 'income_group', 'smoking_status',
       'alcohol_consumption', 'binge_drinking', 'heavy_drinking',
       'difficulty_walking']

st.write(len(cols))
st.write(len(question_answers))


df = pd.DataFrame([question_answers], columns=cols)  

column_transformer = joblib.load("column_transformer.joblib.diab")

pred = column_transformer.transform(df)

ans = model.predict(pred)

if ans = 1:
  st.write("The Logisitic Regression models has predicted you are diabetic")
if ans = 0:
 st.write("The Logistic Regression model has predicted you aren't diabetic")
