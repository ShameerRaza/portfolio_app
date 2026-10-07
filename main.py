import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Shameer Raza | Home", page_icon="👋", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.sidebar.success("Select a page above to navigate.")

col1, col2 = st.columns((2, 1))
with col1:
    st.title("Hi, I'm Shameer Raza 👋")
    st.subheader("MIS Analyst | Data Analyst")
    st.write("Transforming raw data into meaningful business insights.")
    if st.button("Get in Touch"):
        st.switch_page("pages/6_📬_Contact.py")

with col2:
    lottie_url = "https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=300, key="hero")
