import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📬", layout="wide")

st.header("📬 Contact Me")

col1, col2 = st.columns(2)
with col1:
    st.write("**Email:** shameerraza11@gmail.com")
    st.write("**Phone:** +91 7903421534")
    st.write("**LinkedIn:** [linkedin.com/in/shameerraza](#)")
    st.write("**Address:** Chapra, Bihar, India 841415")
    
with col2:
    with st.form("contact_form"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Message sent successfully! (UI Simulation)")
