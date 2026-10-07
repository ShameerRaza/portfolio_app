import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👤", layout="wide")

st.header(" About Me")
col1, col2 = st.columns((1, 3))

with col1:
    try:
        st.image("assets/profile_pic.png", width=250)
    except:
        st.info("Profile picture goes here (assets/profile_pic.png)")

with col2:
    st.write("""
    I am a motivated Computer Science graduate with practical experience in **Artificial Intelligence, AWS Cloud Computing, SQL, Python, Power BI, Advanced Excel, Looker Studio, and Computer Networking**. 
    
    Through internships and professional training, I have developed strong analytical, reporting, dashboard development, and problem-solving skills. I am passionate about transforming raw data into meaningful business insights and eager to grow as an MIS Analyst, Data Analyst, Business Analyst, or Power BI Developer.
    """)
    st.write("**📍 Location:** Kolkata, West Bengal, India")
    st.write("**🎓 Education:** B.Tech, Computer Science & Engineering (8.11 CGPA)")
    st.write("**🌐 Languages:** English, Hindi, Urdu, Bengali")
