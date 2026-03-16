import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import base64

from resume_skill_parser import extract_skills
from career_match_engine import career_matches
from readiness_engine import calculate_readiness
from roadmap_engine import generate_learning_roadmap
from insights_engine import generate_insights


st.set_page_config(
    page_title="AI Resume Intelligence",
    layout="wide"
)


# BACKGROUND

def set_background():

    with open("analyzer/Resume_AI_Project/ai_background.jpg", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        }}

        .glass {{
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(14px);
        border-radius: 14px;
        padding: 25px;
        border:1px solid rgba(255,255,255,0.2);
        }}

        h1 {{
        font-family: 'Trebuchet MS';
        letter-spacing:2px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background()


# TITLE

st.markdown(
"""
<h1 style='text-align:center;
color:#00E5FF;
font-size:45px;
font-weight:800;
'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""",
unsafe_allow_html=True
)


# SIDEBAR

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    ["Dashboard","Skill Analysis","Career Recommendation","Skill Gap Detector"]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Resume",
    type=["pdf","docx","txt"]
)


if uploaded_file is None:

    st.info("Upload your resume from the sidebar to begin analysis.")
    st.stop()


# PROCESS RESUME

skills = extract_skills(uploaded_file)

career_scores = career_matches(skills)

score = calculate_readiness(skills)

roadmap = generate_learning_roadmap(skills)

insights = generate_insights(skills)


# DASHBOARD

if page == "Dashboard":

    col1,col2 = st.columns(2)

    with col1:

        st.markdown("<div class='glass'>",unsafe_allow_html=True)

        st.subheader("Resume Score")

        fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        title = {'text': "Resume Strength"},
        gauge = {
        'axis': {'range':[0,100]},
        'bar': {'color':"#00E5FF"},
        'steps':[
        {'range':[0,40],'color':"#ff4d4d"},
        {'range':[40,70],'color':"#ffa64d"},
        {'range':[70,100],'color':"#00ffcc"}
        ]}
        ))

        st.plotly_chart(fig,use_container_width=True)

        st.markdown("</div>",unsafe_allow_html=True)


    with col2:

        st.markdown("<div class='glass'>",unsafe_allow_html=True)

        st.subheader("AI Insights")

        for i in insights:
            st.write("•",i)

        st.markdown("</div>",unsafe_allow_html=True)



# SKILL ANALYSIS

if page == "Skill Analysis":

    st.markdown("<div class='glass'>",unsafe_allow_html=True)

    st.subheader("Detected Skills")

    skill_names = skills
    skill_values = [1]*len(skills)

    fig = px.bar(
    y=skill_names,
    x=skill_values,
    orientation="h",
    color=skill_names,
    title="Skill Distribution",
    )

    fig.update_layout(
    showlegend=False,
    xaxis_title="Skill Presence",
    yaxis_title="Skills"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>",unsafe_allow_html=True)



# CAREER RECOMMENDATION

if page == "Career Recommendation":

    st.markdown("<div class='glass'>",unsafe_allow_html=True)

    st.subheader("Recommended Career Paths")

    labels = list(career_scores.keys())

    values = list(career_scores.values())

    fig = go.Figure(
        data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.55
        )]
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown("</div>",unsafe_allow_html=True)



# SKILL GAP

if page == "Skill Gap Detector":

    st.markdown("<div class='glass'>",unsafe_allow_html=True)

    st.subheader("Learning Roadmap")

    for skill,steps in roadmap.items():

        st.markdown(f"### {skill}")

        for step in steps:
            st.write("•",step)

    st.markdown("</div>",unsafe_allow_html=True)
