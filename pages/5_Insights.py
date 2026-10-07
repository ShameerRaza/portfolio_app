import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(page_title="Insights", page_icon="📈", layout="wide")

PLOTLY_THEME = {
    "layout": go.Layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#ccd6f6"), colorway=["#64ffda", "#48b0f7", "#a8b2d1"]
    )
}
pio.templates["custom_theme"] = PLOTLY_THEME
pio.templates.default = "custom_theme"

@st.cache_data
def load_analytics():
    return pd.read_csv("data/analytics.csv")

st.header("📈 Skill Growth Insights")
st.write("An animated look at how my core analytical skills have progressed over the years.")

df_analytics = load_analytics().sort_values("Year")

fig_anim = px.bar(
    df_analytics, x="Skill", y="Proficiency", 
    animation_frame="Year", animation_group="Skill",
    range_y=[0, 10], color="Skill",
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_anim, use_container_width=True)
