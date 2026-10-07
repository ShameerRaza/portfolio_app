import os

# 1. Define folder structure
base_dir = "portfolio_app"
folders = [
    f"{base_dir}/.streamlit",
    f"{base_dir}/data",
    f"{base_dir}/assets"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# 2. Define file contents
files = {
    f"{base_dir}/requirements.txt": """streamlit
pandas
plotly
streamlit-lottie
requests
""",
    f"{base_dir}/.streamlit/config.toml": """[theme]
primaryColor = "#64ffda"
backgroundColor = "#0a192f"
secondaryBackgroundColor = "#112240"
textColor = "#ccd6f6"
font = "sans serif"

[server]
headless = true
""",
    f"{base_dir}/data/skills.csv": """Skill,Category,Level
SQL,Data Analysis,9
Power BI,Data Analysis,9
Advanced Excel,Data Analysis,9
Looker Studio,Data Analysis,8
Python,Programming,8
HTML/CSS,Programming,6
MATLAB,Programming,5
AWS (EC2 S3 IAM),Cloud & Tools,7
Computer Networking,Cloud & Tools,7
Microsoft Office,Cloud & Tools,9
""",
    f"{base_dir}/data/projects.csv": """Title,Description,TechStack,Link
AI-Powered Mutual Fund Recommendation System,Machine learning-based recommendation system with feature engineering and predictive analytics to generate investment recommendations.,Python, Machine Learning,#
AI Exam Proctoring System,Automated online examination monitoring system with face detection eye tracking and basic cheating detection features.,Python, OpenCV,#
""",
    f"{base_dir}/data/experience.csv": """Role,Organization,Type,Start,End
MIS Analyst Training,ICA Edu Skills,Experience,2026-02-01,2026-10-07
AWS Cloud Intern,Webguru Infosystems,Experience,2024-08-01,2024-10-01
AI & Machine Learning Intern,Rinex Technology,Experience,2022-09-01,2022-11-01
B.Tech CSE,Brainware University,Education,2021-08-01,2025-07-01
Higher Secondary,Bihar Board of Open Schooling,Education,2019-01-01,2021-01-01
""",
    f"{base_dir}/data/analytics.csv": """Year,Skill,Proficiency
2022,Python,4
2022,SQL,3
2022,Power BI,1
2024,Python,6
2024,SQL,6
2024,Power BI,5
2026,Python,8
2026,SQL,9
2026,Power BI,9
""",
    f"{base_dir}/app.py": """import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie

# -----------------------------------------------------------------------------
# PAGE CONFIG & SETUP
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Shameer Raza | Portfolio", page_icon="📊", layout="wide")

PLOTLY_THEME = {
    "layout": go.Layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#ccd6f6"),
        colorway=["#64ffda", "#48b0f7", "#a8b2d1"]
    )
}
import plotly.io as pio
pio.templates["custom_theme"] = PLOTLY_THEME
pio.templates.default = "custom_theme"

@st.cache_data
def load_data(filename):
    return pd.read_csv(f"data/{filename}")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_hero():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Hi, I'm Shameer Raza 👋")
        st.subheader("MIS Analyst | Data Analyst")
        st.write("Transforming raw data into meaningful business insights.")
        st.markdown("[📥 Download Resume](#contact)")
    with col2:
        lottie_url = "https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json"
        lottie_json = load_lottieurl(lottie_url)
        if lottie_json:
            st_lottie(lottie_json, height=250, key="hero_animation")

def render_about():
    st.markdown("---")
    st.header("👤 About Me")
    col1, col2 = st.columns((1, 3))
    with col1:
        try:
            st.image("assets/profile_pic.png", width=200)
        except:
            st.info("Place 'profile_pic.png' in the assets folder.")
    with col2:
        st.write(\"\"\"
        I am a motivated Computer Science graduate with practical experience in **Artificial Intelligence, AWS Cloud Computing, SQL, Python, Power BI, Advanced Excel, Looker Studio, and Computer Networking**. 
        
        Through internships and professional training, I have developed strong analytical, reporting, dashboard development, and problem-solving skills. I am passionate about transforming raw data into meaningful business insights and eager to grow as an MIS Analyst or Power BI Developer.
        \"\"\")
        st.write("**📍 Location:** Kolkata, West Bengal, India")
        st.write("**🎓 Education:** B.Tech, Computer Science & Engineering (8.11 CGPA)")

def render_skills():
    st.markdown("---")
    st.header("🛠️ Technical Skills")
    df_skills = load_data("skills.csv")
    categories = df_skills["Category"].unique()
    selected_cats = st.multiselect("Filter by Category", categories, default=categories)
    filtered_df = df_skills[df_skills["Category"].isin(selected_cats)]
    
    col1, col2 = st.columns(2)
    with col1:
        if not filtered_df.empty:
            fig_radar = go.Figure(data=go.Scatterpolar(
                r=filtered_df["Level"],
                theta=filtered_df["Skill"],
                fill='toself',
                line_color="#64ffda"
            ))
            fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])))
            st.plotly_chart(fig_radar, use_container_width=True)
    with col2:
        if not filtered_df.empty:
            fig_bar = px.bar(
                filtered_df.sort_values(by="Level", ascending=True), 
                x="Level", y="Skill", orientation='h',
                color="Category",
                color_discrete_sequence=["#64ffda", "#48b0f7", "#a8b2d1"]
            )
            fig_bar.update_layout(showlegend=False)
            st.plotly_chart(fig_bar, use_container_width=True)

def render_projects():
    st.markdown("---")
    st.header("🚀 Academic Projects")
    df_projects = load_data("projects.csv")
    all_techs = set([tech.strip() for sublist in df_projects["TechStack"].str.split(',') for tech in sublist])
    selected_tech = st.multiselect("Filter by Technology", list(all_techs))
    
    if selected_tech:
        mask = df_projects["TechStack"].apply(lambda x: any(t in x for t in selected_tech))
        df_projects = df_projects[mask]
        
    for _, row in df_projects.iterrows():
        with st.container():
            st.subheader(row["Title"])
            st.write(f"**Tech Stack:** {row['TechStack']}")
            st.write(row["Description"])
            st.markdown(f"[View Project]({row['Link']})")
            st.markdown("<br>", unsafe_allow_html=True)

def render_experience():
    st.markdown("---")
    st.header("⏳ Experience & Education Timeline")
    df_exp = load_data("experience.csv")
    df_exp["Start"] = pd.to_datetime(df_exp["Start"])
    df_exp["End"] = pd.to_datetime(df_exp["End"])
    fig_time = px.timeline(
        df_exp, x_start="Start", x_end="End", y="Role", 
        color="Type", hover_name="Organization",
        color_discrete_map={"Experience": "#64ffda", "Education": "#48b0f7"}
    )
    fig_time.update_yaxes(autorange="reversed") 
    st.plotly_chart(fig_time, use_container_width=True)

def render_analytics():
    st.markdown("---")
    st.header("📈 Skill Growth Insights")
    st.write("An animated look at how my core analytical skills have progressed.")
    df_analytics = load_data("analytics.csv")
    fig_anim = px.bar(
        df_analytics, x="Skill", y="Proficiency", 
        animation_frame="Year", animation_group="Skill",
        range_y=[0, 10], color="Skill",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_anim, use_container_width=True)

def render_contact():
    st.markdown("---")
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

def render_footer():
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #8892b0;'>© 2026 Shameer Raza. Built entirely with Python & Streamlit.</p>", unsafe_allow_html=True)

def main():
    render_hero()
    render_about()
    render_skills()
    render_projects()
    render_experience()
    render_analytics()
    render_contact()
    render_footer()

if __name__ == "__main__":
    main()
"""
}

# 3. Create all files
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Success! Your complete '{base_dir}' folder has been created.")
print(f"You can now place your CV photo at '{base_dir}/assets/profile_pic.png'.")
