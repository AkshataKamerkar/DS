
import streamlit as st
import os
from email.message import EmailMessage
import ssl
import smtplib

st.title("Contact Us")

mail_user = os.environ.get('TestUser')
mail_pass = os.environ.get('TestUserPass')


def GenEmail(email,name):

    subject = "Thank you for contacting us!"
    body = '''
    Dear {},
        Thank you for contacting us through our website's contact form. Our team has received your message and we will get back to you as soon as possible. We strive to provide prompt and helpful responses to all inquiries.
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


with st.form("Test form"):
    name = st.text_input("Enter your Name : ")
    email = st.text_input("Enter your Email-Id : ")
    query = st.text_input("Enter your query : ")
    
    if(st.form_submit_button("Submit")):
        GenEmail(email, name)
        st.success("Submitted Successfully ! ")
        
        


