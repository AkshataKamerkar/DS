# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:32:59 2023

@author: DELL
"""

import streamlit as st
import sqlite3
import os
from email.message import EmailMessage
import ssl
import smtplib

conn = sqlite3.connect('data.db',check_same_thread=False)
cur = conn.cursor()
mail_user = os.environ.get('TestUser')
mail_pass = os.environ.get('TestUserPass')


def isAva(x,ava):
    if(ava[x-1] < 5):
        return True
    return False

ava = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def addData(name,email,disease,query):
    if(disease == "Diabetes"):
        cur.execute("INSERT INTO diab VALUES (?,?,?,?)",(name,email,disease,query));
        conn.commit()
        conn.close()
    elif(disease == "Heart"):
        cur.execute("INSERT INTO heart VALUES (?,?,?,?)",(name,email,disease,query));
        conn.commit()
        conn.close()
        
    elif(disease == "Parkinson"):
        cur.execute("INSERT INTO park VALUES (?,?,?,?)",(name,email,disease,query));
        conn.commit()
        conn.close()
    
        
def GenEmail(email,name):

    subject = "Appointment Booking Confirmation"
    body = '''
    Dear {},
        We are pleased to confirm the details of your appointment scheduled for [Date]. We appreciate your trust in our services and we look forward to meeting you on [Date] regarding your disease treatment.
        Thank you for choosing our services. We look forward to seeing you soon.
    
    Best regards,
    MultipleDiseasePredictionSystem
    '''.format(name)
    
    
    em = EmailMessage()
    em['From'] = mail_user
    em['To']  = email
    em['Subject'] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context= context) as smtp:
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(mail_user,email,em.as_string())

st.title("Appointment Booking")

#date = st.number_input("Please Enter a Date : ",step = 1)
#if(st.button("Check")):
 #   if(isAva(date, ava)):
        #st.write("Date Avaiable !")
st.write("Please fill the details ")
with st.form(key = "Booking Form", clear_on_submit= True):
   name = st.text_input("Enter your Name : ")
   email = st.text_input("Enter your Email-Id : ")
   disease = st.text_input("Enter the Disease : ")
   query = st.text_input("Enter the Query : ")
 
   # Every form must have a submit button.
   
   if(st.form_submit_button("Submit")):
       #ava[date-1] += 1
       addData(name, email, disease, query)
       GenEmail(email, name)
       st.success("Submitted Successfully")
             
               
   # else:
    #   st.warning("Date Not Available !")
                
              
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          


                






















