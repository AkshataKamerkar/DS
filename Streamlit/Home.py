import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title= "HomePage",
    page_icon= "👋",
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(filepath : str):
    with open(filepath,'r') as f:
        return json.load(f)

title, title_ani = st.columns([3,1])

with title:
    st.title("Welcome To :blue[D'Predicto] ")
    st.text("")
    st.text("")
    st.markdown("*Empowering early disease detection and personalized prevention with our advanced Disease Prediction System*")


wel_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_zpjfsp1e.json")
#wel_lottie = load_lottiefile(r'C:\Users\DELL\Downloads\Generic.json')
with title_ani : 
    st_lottie(
        wel_lottie,
        speed = 1,
        reverse = False,
        loop = True,
        quality = "medium",
        height = None,
        width = None,
        key = None,
    )
    
st.text("")
st.text("")
st.subheader("Our Offerings")

st.text("")
st.text("")

prediction, AptBk, Assis = st.columns(3)

pred = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_gkgqj2yq.json")
apt = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_hYRKYxxvdX.json")
bot = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_g7zx4ni5.json")

with prediction:
    st_lottie(
        pred,
        speed = 1,
        reverse = False,
        loop = True,
        quality = "medium",
        height = 220
        )
prediction.markdown('<h4 style = "text-align: center">Prediction System ', unsafe_allow_html = True)

with AptBk:
    st_lottie(
        apt,
        speed = 1,
        reverse = False,
        loop = True,
        quality = "medium"
        )
AptBk.markdown('<h4 style = "text-align: center">Appointment Booking ', unsafe_allow_html = True)

with Assis:
    st_lottie(
        bot,
        speed = 1,
        reverse = False,
        loop = True,
        quality = "medium"
        )
Assis.markdown('<h4 style = "text-align: center">Assistance', unsafe_allow_html = True)



st.text('')
st.text("")
st.text("")

st.subheader("Disease :red[Predicion]")
st.text("")

diab, heart, park = st.columns(3)

dimg = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tbjuenb2.json")
with diab:
    st.text("")
    st.text("")
    st.text("")
    st_lottie(
        dimg,
        speed = 1,
        reverse = False,
        loop = True,
        quality = "medium"
        )
    st.text("")
    st.text("")
    st.text("")

   
diab.markdown('<h4 style = "text-align: center">Diabetes', unsafe_allow_html = True)
    
    
himg = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_a3ntzciy.json")
with heart:
    st_lottie(
        himg,
        speed = 1,
        reverse = False,
        loop = True,
        quality = "medium"
        )
heart.markdown('<h4 style = "text-align: center">Heart Disease', unsafe_allow_html = True)

pimg = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_9NxFrGo71i.json")
with park:
    st_lottie(
        pimg,
        speed = 1,
        reverse = False,
        loop = True,
        quality = "medium"
        )

park.markdown('<h4 style = "text-align: center">Parkinson Disease', unsafe_allow_html = True)


















