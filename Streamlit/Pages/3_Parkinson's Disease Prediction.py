import pickle
import streamlit as st
import pandas as pd
#import plotly.graph_objects as go

# Loading the saved model

heart_model = pickle.load(open(r'C:\Users\DELL\Desktop\Streamlit\SavedModels\park_trained_model.sav','rb'))

# page title
st.title("Parkinson's Disease Prediction using ML")

col1, col2, col3, col4, col5 = st.columns(5)  

with col1:
    fo = st.text_input('MDVP:Fo(Hz)')
    
with col2:
    fhi = st.text_input('MDVP:Fhi(Hz)')
    
with col3:
    flo = st.text_input('MDVP:Flo(Hz)')
    
with col4:
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    
with col5:
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    
with col1:
    RAP = st.text_input('MDVP:RAP')
    
with col2:
    PPQ = st.text_input('MDVP:PPQ')
    
with col3:
    DDP = st.text_input('Jitter:DDP')
    
with col4:
    Shimmer = st.text_input('MDVP:Shimmer')
    
with col5:
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
with col1:
    APQ3 = st.text_input('Shimmer:APQ3')
    
with col2:
    APQ5 = st.text_input('Shimmer:APQ5')
    
with col3:
    APQ = st.text_input('MDVP:APQ')
    
with col4:
    DDA = st.text_input('Shimmer:DDA')
    
with col5:
    NHR = st.text_input('NHR')
    
with col1:
    HNR = st.text_input('HNR')
    
with col2:
    RPDE = st.text_input('RPDE')
    
with col3:
    DFA = st.text_input('DFA')
    
with col4:
    spread1 = st.text_input('spread1')
    
with col5:
    spread2 = st.text_input('spread2')
    
with col1:
    D2 = st.text_input('D2')
    
with col2:
    PPE = st.text_input('PPE')
    


# code for Prediction
parkinsons_diagnosis = ''

# creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
    
    if (parkinsons_prediction[0] == 1):
      parkinsons_diagnosis = "The person has Parkinson's disease"
    else:
      parkinsons_diagnosis = "The person does not have Parkinson's disease"
    
st.success(parkinsons_diagnosis)


st.write("Not Sure about the Parameters ?")

excel_file = r'C:\Users\DELL\Desktop\Streamlit\Pages\PP.xlsx'
sheet_name = 'Data'

df = pd.read_excel(excel_file, sheet_name= sheet_name, usecols= 'A:B', header= 0)

if st.button("Click Here"):
    # Try to create a table using plotly
    st.dataframe(df)
    

