import streamlit as st
import pandas as pd

st.set_page_config(page_title="Projects", page_icon="🚀", layout="wide")

@st.cache_data
def load_projects():
    return pd.read_csv("data/projects.csv")

st.header("🚀 Academic & Professional Projects")
df_projects = load_projects()

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
        st.divider()
