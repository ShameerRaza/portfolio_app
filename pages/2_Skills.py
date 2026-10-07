import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(page_title="Skills", page_icon="🛠️", layout="wide")

PLOTLY_THEME = {
    "layout": go.Layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#ccd6f6"), colorway=["#64ffda", "#48b0f7", "#a8b2d1"]
    )
}
pio.templates["custom_theme"] = PLOTLY_THEME
pio.templates.default = "custom_theme"

@st.cache_data
def load_skills():
    return pd.read_csv("data/skills.csv")

st.header("🛠️ Technical Skills")
df_skills = load_skills()

categories = df_skills["Category"].unique()
selected_cats = st.multiselect("Filter by Category", categories, default=categories)
filtered_df = df_skills[df_skills["Category"].isin(selected_cats)]

col1, col2 = st.columns(2)
with col1:
    if not filtered_df.empty:
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=filtered_df["Level"], theta=filtered_df["Skill"], fill='toself', line_color="#64ffda"
        ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])))
        st.plotly_chart(fig_radar, use_container_width=True)

with col2:
    if not filtered_df.empty:
        fig_bar = px.bar(
            filtered_df.sort_values(by="Level", ascending=True), 
            x="Level", y="Skill", orientation='h', color="Category",
            color_discrete_sequence=["#64ffda", "#48b0f7", "#a8b2d1"]
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)
