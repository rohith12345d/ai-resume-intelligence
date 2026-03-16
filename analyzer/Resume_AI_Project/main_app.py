import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import base64

from resume_skill_parser import extract_skills
from career_match_engine import career_matches
from readiness_engine import calculate_readiness
from roadmap_engine import generate_learning_roadmap
from insights_engine import generate_insights


# PAGE CONFIG
st.set_page_config(
    page_title="AI RESUME INTELLIGENCE",
    page_icon="🧠",
    layout="wide"
)


# BACKGROUND IMAGE
def set_background():

    with open("analyzer/Resume_AI_Project/ai_background.jpg", "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

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
        margin-bottom: 25px;
        border:1px solid rgba(255,255,255,0.15);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background()


# TITLE
st.markdown(
"""
<h1 style='
text-align:center;
font-size:42px;
color:#00E5FF;
font-weight:800;
letter-spacing:2px;
'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""",
unsafe_allow_html=True
)

st.write("")


# SIDEBAR
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    ["Dashboard", "Skill Analysis", "Career Recommendation", "Skill Gap Detector"]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Resume",
    type=["pdf","docx","txt"]
)


# IF NO FILE
if uploaded_file is None:

    st.info("Upload your resume from the sidebar to begin analysis.")
    st.stop()


# PROCESS RESUME
skills = extract_skills(uploaded_file)
careers = career_matches(skills)
score = calculate_readiness(skills)
roadmap = generate_learning_roadmap(skills)
insights = generate_insights(skills)


# DASHBOARD
if page == "Dashboard":

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("Resume Score")

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        title = {'text': "Resume Strength"},
        gauge = {
            'axis': {'range': [0,100]},
            'bar': {'color': "#00E5FF"},
            'steps' : [
                {'range': [0,40], 'color': "#FF4B4B"},
                {'range': [40,70], 'color': "#FFA500"},
                {'range': [70,100], 'color': "#00FFB3"}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("AI Insights")

    for i in insights:
        st.write("•", i)

    st.markdown("</div>", unsafe_allow_html=True)


# SKILL ANALYSIS
if page == "Skill Analysis":

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("Detected Skills")

    skill_names = list(skills.keys())
    skill_values = list(skills.values())

    fig, ax = plt.subplots()

    ax.bar(skill_names, skill_values)

    plt.xticks(rotation=30)

    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)


# CAREER RECOMMENDATION
if page == "Career Recommendation":

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("Recommended Careers")

    labels = list(careers.keys())
    values = list(careers.values())

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.5
    )])

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


# SKILL GAP
if page == "Skill Gap Detector":

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("Learning Roadmap")

    for skill, steps in roadmap.items():

        st.markdown(f"### {skill}")

        for s in steps:
            st.write("•", s)

    st.markdown("</div>", unsafe_allow_html=True)
