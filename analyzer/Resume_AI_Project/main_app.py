import streamlit as st
import plotly.graph_objects as go
import base64
import os

from resume_skill_parser import extract_skills
from career_match_engine import recommend_roles
from readiness_engine import calculate_readiness
from roadmap_engine import generate_learning_roadmap
from insights_engine import generate_insights


# PAGE CONFIG
st.set_page_config(page_title="AI Resume Intelligence", layout="wide")


# BACKGROUND
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
        background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_background()


# TITLE
st.markdown("""
<h1 style='text-align:center;color:#00E5FF;font-weight:800'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""", unsafe_allow_html=True)


# SIDEBAR NAVIGATION
st.sidebar.title("AI Resume Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    ["Skill Analysis", "Career Match", "Skill Gap Roadmap", "AI Insights"]
)


# FILE UPLOAD
uploaded_file = st.sidebar.file_uploader(
    "Upload Resume",
    type=["txt", "pdf", "docx"]
)

if uploaded_file is None:
    st.info("Upload your resume from the sidebar to begin analysis")
    st.stop()


# SKILL EXTRACTION
skills = extract_skills(uploaded_file)

if not skills or len(skills) == 0:
    st.warning("No skills detected in resume")
    st.stop()


skill_names = []
skill_values = []

for skill, count in skills.items():
    skill_names.append(skill)
    skill_values.append(count)


# limit to top skills (clean UI)
skill_names = skill_names[:10]
skill_values = skill_values[:10]


# RESUME SCORE
score = calculate_readiness(skill_names)

fig_meter = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    number={'font': {'size': 45, 'color': "#00E5FF"}},
    title={'text': "Resume Strength", 'font': {'size': 22, 'color': "#00E5FF"}},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#00E5FF"},
        'bgcolor': "rgba(0,0,0,0.6)",
        'steps': [
            {'range': [0, 40], 'color': "#330000"},
            {'range': [40, 70], 'color': "#332200"},
            {'range': [70, 100], 'color': "#003333"}
        ]
    }
))

fig_meter.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    font={'color': "#00E5FF"}
)


# SKILL ANALYSIS
if menu == "Skill Analysis":

    st.subheader("Resume Strength")

    st.plotly_chart(fig_meter, use_container_width=True)

    st.subheader("Detected Skills")

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=skill_values,
        y=skill_names,
        orientation='h',
        marker=dict(color="#00E5FF")
    ))

    fig.update_layout(
        title="Skill Strength",
        xaxis_title="Frequency",
        yaxis_title="Skills",
        height=450,
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)


# CAREER MATCH
elif menu == "Career Match":

    st.subheader("Career Recommendations")

    roles = recommend_roles(skill_names)

    if roles:

        labels = list(roles.keys())
        values = list(roles.values())

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.55
        )])

        fig.update_layout(
            title="Career Match Distribution",
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("No matching career roles found")


# SKILL GAP ROADMAP
elif menu == "Skill Gap Roadmap":

    st.subheader("Learning Roadmap")

    roadmap = generate_learning_roadmap(skill_names)

    for skill, steps in roadmap.items():

        st.markdown(f"### {skill}")

        for step in steps:
            st.write("•", step)


# AI INSIGHTS
elif menu == "AI Insights":

    st.subheader("AI Resume Insights")

    insights = generate_insights(skill_names)

    for insight in insights:
        st.write("•", insight)
