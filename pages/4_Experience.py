import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(page_title="Experience", page_icon="⏳", layout="wide")

PLOTLY_THEME = {
    "layout": go.Layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#ccd6f6"), colorway=["#64ffda", "#48b0f7", "#a8b2d1"]
    )
}
pio.templates["custom_theme"] = PLOTLY_THEME
pio.templates.default = "custom_theme"

@st.cache_data
def load_experience():
    return pd.read_csv("data/experience.csv")

st.header("⏳ Experience & Education Timeline")
df_exp = load_experience()
df_exp["Start"] = pd.to_datetime(df_exp["Start"])
df_exp["End"] = pd.to_datetime(df_exp["End"])

fig_time = px.timeline(
    df_exp, x_start="Start", x_end="End", y="Role", 
    color="Type", hover_name="Organization",
    color_discrete_map={"Experience": "#64ffda", "Education": "#48b0f7"}
)
fig_time.update_yaxes(autorange="reversed") 
st.plotly_chart(fig_time, use_container_width=True)
