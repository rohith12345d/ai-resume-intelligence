import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import base64
import os

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
# BACKGROUND IMAGE + GLASS CSS
# -----------------------------

def set_background():

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "ai_background.jpg")

    with open(image_path, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        }}

        .glass-card {{
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(14px);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        border:1px solid rgba(255,255,255,0.2);
        box-shadow:0 8px 32px rgba(0,0,0,0.35);
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
<h1 style='
text-align:center;
color:#00E5FF;
font-weight:800;
letter-spacing:3px;
font-size:42px;
'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""",
unsafe_allow_html=True
)

st.markdown("<hr style='border:1px solid #00E5FF;'>", unsafe_allow_html=True)


# -----------------------------
# FILE UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
"Upload Resume (PDF / DOCX / TXT)"
)

if uploaded_file is None:
    st.info("Please upload your resume to begin analysis.")
    st.stop()


# -----------------------------
# SKILL EXTRACTION
# -----------------------------

detected_skills = extract_skills(uploaded_file)

if not detected_skills:
    st.warning("No skills detected in resume.")
    st.stop()

all_skills = []
all_counts = []

for category, skills in detected_skills.items():
    for skill, count in skills.items():
        all_skills.append(skill)
        all_counts.append(count)

# -----------------------------
# RESUME SCORE
# -----------------------------

score = calculate_readiness(all_skills)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

st.subheader("AI Resume Strength Meter")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    number={'font': {'size': 48, 'color': "#00E5FF"}},
    title={'text': "<b>Resume Score</b>", 'font': {'size': 22, 'color': "#00E5FF"}},
    gauge={
        'axis': {'range': [0, 100], 'tickcolor': "#00E5FF"},
        'bar': {'color': "#00E5FF", 'thickness': 0.35},
        'bgcolor': "rgba(0,0,0,0.6)",
        'borderwidth': 2,
        'bordercolor': "#00E5FF",
        'steps': [
            {'range': [0, 40], 'color': "#2b0a0a"},
            {'range': [40, 70], 'color': "#332200"},
            {'range': [70, 100], 'color': "#003333"}
        ]
    }
))

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    font={'color': "#00E5FF"}
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# SKILL ANALYSIS
# -----------------------------

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

st.subheader("Skill Analysis")

fig = px.bar(
    y=all_skills,
    x=all_counts,
    orientation="h",
    color=all_skills,
    title="Skill Strength in Resume"
)

fig.update_layout(
    showlegend=False,
    height=400,
    xaxis_title="Frequency",
    yaxis_title="Skills"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# CAREER MATCH
# -----------------------------

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

st.subheader("Career Recommendations")

roles = recommend_roles(all_skills)

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

st.plotly_chart(fig, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# SKILL GAP ROADMAP
# -----------------------------

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

st.subheader("Skill Gap Roadmap")

roadmap = generate_learning_roadmap(all_skills)

for skill, steps in roadmap.items():

    st.markdown(f"### {skill}")

    for step in steps:
        st.write("•", step)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# AI INSIGHTS
# -----------------------------

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

st.subheader("AI Resume Insights")

insights = generate_insights(all_skills)

for insight in insights:
    st.write("•", insight)

st.markdown("</div>", unsafe_allow_html=True)
