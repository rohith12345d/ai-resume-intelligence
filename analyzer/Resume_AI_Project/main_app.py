import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import base64

from resume_skill_parser import extract_skills
from career_match_engine import recommend_roles
from readiness_engine import calculate_readiness
from roadmap_engine import generate_learning_roadmap
from insights_engine import generate_insights

#-----------------------------

# PAGE CONFIG

#-----------------------------

st.set_page_config(
page_title="AI Resume Intelligence",
layout="wide"
)

#-----------------------------

# BACKGROUND

#-----------------------------

def set_background():

    with open("ai_background.jpg","rb") as f:
        img = base64.b64encode(f.read()).decode()

st.markdown(
f"""
<style>

.stApp {{
background-image: url("data:image/jpg;base64,{img}");
background-size: cover;
background-attachment: fixed;
}}

.glass {{
background: rgba(255,255,255,0.08);
backdrop-filter: blur(12px);
padding: 25px;
border-radius: 12px;
border: 1px solid rgba(255,255,255,0.2);
}}

</style>
""",
unsafe_allow_html=True
)

set_background()

#-----------------------------

# TITLE

#-----------------------------

st.markdown(
"""

<h1 style='text-align:center;color:#00E5FF;font-weight:800'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""",
unsafe_allow_html=True
)
st.write("")

#-----------------------------

# SIDEBAR NAVIGATION

#-----------------------------

st.sidebar.title("AI Resume Dashboard")

menu = st.sidebar.radio(
"Navigation",
[
"Skill Analysis",
"Career Match",
"Skill Gap Roadmap",
"AI Insights"
]
)

#-----------------------------

# FILE UPLOAD

#-----------------------------

uploaded_file = st.sidebar.file_uploader(
"Upload Resume",
type=["txt","pdf","docx"]
)

if uploaded_file is None:
st.info("Upload your resume from the sidebar to begin analysis")
st.stop()

#-----------------------------

# SKILL EXTRACTION

#-----------------------------

skills = extract_skills(uploaded_file)

if not skills:
st.warning("No skills detected in resume")
st.stop()

skill_names = list(skills.keys())
skill_values = list(skills.values())

#-----------------------------

# RESUME SCORE

#-----------------------------

score = calculate_readiness(skill_names)

fig_meter = go.Figure(go.Indicator(

mode="gauge+number",
value=score,

number={'font':{'size':45,'color':"#00E5FF"}},

title={'text':"Resume Strength",'font':{'size':22,'color':"#00E5FF"}},

gauge={
'axis':{'range':[0,100]},
'bar':{'color':"#00E5FF"},
'bgcolor':"rgba(0,0,0,0.6)",

'steps':[
{'range':[0,40],'color':"#330000"},
{'range':[40,70],'color':"#332200"},
{'range':[70,100],'color':"#003333"}
]

}

))

fig_meter.update_layout(
paper_bgcolor="rgba(0,0,0,0)",
font={'color':"#00E5FF"}
)

#-----------------------------

# DASHBOARD PANEL

#-----------------------------

st.plotly_chart(fig_meter,use_container_width=True)

st.markdown("<div class='glass'>",unsafe_allow_html=True)

#-----------------------------

# SKILL ANALYSIS

#-----------------------------

if menu == "Skill Analysis":

st.subheader("Detected Skills")

fig = px.bar(
    x=skill_values,
    y=skill_names,
    orientation="h",
    title="Skill Strength"
)

fig.update_layout(
height=450,
showlegend=False
)

st.plotly_chart(fig,use_container_width=True)

#-----------------------------

# CAREER MATCH

#-----------------------------

elif menu == "Career Match":

st.subheader("Career Recommendations")

roles = recommend_roles(skill_names)

labels = list(roles.keys())
values = list(roles.values())

fig = go.Figure(
data=[go.Pie(
labels=labels,
values=values,
hole=0.55
)]
)

st.plotly_chart(fig,use_container_width=True)

#-----------------------------

# SKILL GAP ROADMAP

#-----------------------------

elif menu == "Skill Gap Roadmap":

st.subheader("Learning Roadmap")

roadmap = generate_learning_roadmap(skill_names)

for skill,steps in roadmap.items():

    st.markdown(f"### {skill}")

    for step in steps:
        st.write("•",step)

#-----------------------------

# AI INSIGHTS

#-----------------------------

elif menu == "AI Insights":

st.subheader("AI Resume Insights")

insights = generate_insights(skill_names)

for insight in insights:
    st.write("•",insight)

st.markdown("</div>",unsafe_allow_html=True)
