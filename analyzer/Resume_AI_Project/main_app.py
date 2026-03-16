import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import base64

from resume_skill_parser import extract_skills
from career_match_engine import recommend_roles
from readiness_engine import calculate_readiness
from roadmap_engine import generate_learning_roadmap
from insights_engine import generate_insights

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Resume Intelligence",
    layout="wide"
)

# -----------------------------
# BACKGROUND IMAGE
# -----------------------------

def set_background():

    with open("ai_background.jpg", "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-attachment: fixed;
        }}

        .block-container {{
        background: rgba(0,0,0,0.55);
        padding: 2rem;
        border-radius: 15px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# -----------------------------
# TITLE
# -----------------------------

st.markdown(
"""
<h1 style='text-align:center;
color:#00E5FF;
font-weight:800;
letter-spacing:2px;'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p style='text-align:center;color:white'>
Upload your resume to analyze skills and career opportunities
</p>
""",
unsafe_allow_html=True
)

# -----------------------------
# FILE UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
"Upload Resume",
type=["txt","pdf","docx"]
)

if uploaded_file:

    # -----------------------------
    # SKILL EXTRACTION
    # -----------------------------

    skills = extract_skills(uploaded_file)

    if not skills:
        st.warning("No skills detected in resume.")
        st.stop()

    skill_names = list(skills.keys())
    skill_values = list(skills.values())

    # -----------------------------
    # RESUME SCORE
    # -----------------------------

    score = calculate_readiness(skill_names)

    st.subheader("Resume Strength")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text':"Resume Score"},
        gauge={
            'axis':{'range':[0,100]},
            'bar':{'color':"#00E5FF"},
            'steps':[
                {'range':[0,40],'color':"#FF4D4D"},
                {'range':[40,70],'color':"#FFA500"},
                {'range':[70,100],'color':"#00FFB3"}
            ]
        }
    ))

    st.plotly_chart(fig,use_container_width=True)

    # -----------------------------
    # SKILL ANALYSIS
    # -----------------------------

    st.subheader("Detected Skills")

    fig = px.bar(
        y=skill_names,
        x=skill_values,
        orientation="h",
        color=skill_names,
        title="Skill Strength in Resume"
    )

    fig.update_layout(
        showlegend=False,
        height=400,
        xaxis_title="Frequency",
        yaxis_title="Skills"
    )

    st.plotly_chart(fig,use_container_width=True)

    # -----------------------------
    # CAREER MATCH
    # -----------------------------

    st.subheader("Career Recommendations")

    roles = recommend_roles(skill_names)

    labels = list(roles.keys())
    values = list(roles.values())

    fig = go.Figure(
        data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.55,
            textinfo="label+percent"
        )]
    )

    fig.update_layout(title="Career Match Distribution")

    st.plotly_chart(fig,use_container_width=True)

    # -----------------------------
    # SKILL GAP ROADMAP
    # -----------------------------

    st.subheader("Skill Gap Roadmap")

    roadmap = generate_learning_roadmap(skill_names)

    for skill,steps in roadmap.items():

        st.markdown(f"### {skill}")

        for step in steps:
            st.write("•",step)

    # -----------------------------
    # AI INSIGHTS
    # -----------------------------

    st.subheader("AI Resume Insights")

    insights = generate_insights(skill_names)

    for insight in insights:
        st.write("•",insight)
