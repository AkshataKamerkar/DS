import pickle
import streamlit as st

# Loading the saved model

dia_model = pickle.load(open(r'C:\Users\DELL\Desktop\Streamlit\SavedModels\dia_trained_model.sav','rb'))

# page title
st.title('Diabetes Prediction using ML')


# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
    
with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):
    
# Also do this with other Models 
    if(Pregnancies == "" or Glucose == "" or BloodPressure == "" or SkinThickness == "" or Insulin == "" or BMI == "" or DiabetesPedigreeFunction == "" or Age == "" ):
        st.warning("Please Fill the above fields !!")
        
    else:
        diab_prediction = dia_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          st.success(':red[The person is diabetic]')
          
          st.text("Do you want view the the Top five Specialist for Diabetes")
          if(st.button("Yes")):
              st.text("Coming Soon...")
        else:
          st.success(':blue[The person is not diabetic]')
    

