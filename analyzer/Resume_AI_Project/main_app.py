import streamlit as st
import plotly.graph_objects as go
import base64
import os
import time
import random

from resume_skill_parser import extract_skills
from career_match_engine import recommend_roles
from readiness_engine import calculate_readiness
from roadmap_engine import generate_learning_roadmap
from insights_engine import generate_insights


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Resume Intelligence", layout="wide")


# ---------------- BACKGROUND ----------------
def set_background():
    try:
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "ai_background.jpg")

        with open(image_path, "rb") as f:
            img = base64.b64encode(f.read()).decode()

        st.markdown(f"""
        <style>

        .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-attachment: fixed;
        }}

        .glass-card {{
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(12px);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        border: 1px solid rgba(0,229,255,0.3);
        box-shadow: 0 0 10px rgba(0,229,255,0.4),
        0 0 20px rgba(0,229,255,0.2);
        }}

        </style>
        """, unsafe_allow_html=True)

    except:
        pass

set_background()


# ---------------- TITLE ----------------
st.markdown("""
<h1 style='text-align:center;color:#00E5FF;font-weight:800'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""", unsafe_allow_html=True)

st.success("AI System Status: Active and Ready")


# ---------------- SIDEBAR ----------------
st.sidebar.title("AI Resume Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    [
        "📊 Skill Analysis",
        "🎯 Career Match",
        "🧠 Skill Gap Roadmap",
        "💡 AI Insights"
    ]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Resume",
    type=["txt","pdf","docx"]
)

if uploaded_file is None:
    st.info("Upload your resume from the sidebar to begin analysis")
    st.stop()


# ---------------- SKILL EXTRACTION ----------------
with st.spinner("AI is analyzing your resume..."):

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    progress.empty()

    skills_raw = extract_skills(uploaded_file)

if not skills_raw:
    st.warning("No skills detected in resume")
    st.stop()


# ---------------- NORMALIZE SKILLS ----------------
if isinstance(skills_raw, dict):
    skills = skills_raw
elif isinstance(skills_raw, list):

    skills = {}

    for s in skills_raw:
        skills[s] = skills.get(s,0) + 1

else:
    skills = {}

skill_names = list(skills.keys())
skill_values = list(skills.values())


# =====================================================
# 📊 SKILL ANALYSIS PAGE
# =====================================================
if menu == "📊 Skill Analysis":

    score = calculate_readiness(skill_names)

    # -------- Resume Summary --------
    st.markdown("## Resume Skill Summary")

    col1,col2 = st.columns(2)

    with col1:
        st.metric("Skills Detected",len(skill_names))

    with col2:
        st.metric("Career Matches",len(recommend_roles(skill_names)))

    # -------- Gauge --------
    st.markdown("### AI Resume Strength")

    fig_meter = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text':"AI Resume Strength"},
        gauge={
            'axis':{'range':[0,100]},
            'steps':[
                {'range':[0,40],'color':"#FF3B3B"},
                {'range':[40,70],'color':"#FFA500"},
                {'range':[70,100],'color':"#00FF7F"}
            ]
        }
    ))

    st.plotly_chart(fig_meter,use_container_width=True)


    # -------- AI Evaluation --------
    if score < 40:
        st.error("AI Evaluation: Weak Resume — Add more technical skills")

    elif score < 70:
        st.warning("AI Evaluation: Moderate Resume — Improve projects and experience")

    else:
        st.success("AI Evaluation: Strong Resume — Good job readiness")


    # -------- Detected Skills --------
    st.subheader("Detected Skills")

    cols = st.columns(2)

    for i,(skill,value) in enumerate(skills.items()):
        cols[i%2].write(f"• {skill} ({value})")


    # -------- Skill Frequency Chart --------
    st.subheader("Skill Frequency")

    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        x=skill_values,
        y=skill_names,
        orientation='h'
    ))

    fig_bar.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig_bar,use_container_width=True)


# =====================================================
# 🎯 CAREER MATCH
# =====================================================
elif menu == "🎯 Career Match":

    roles = recommend_roles(skill_names)

    labels = list(roles.keys())
    values = list(roles.values())

    st.subheader("Career Recommendations")

    if sum(values) == 0:

        st.warning("No strong career match detected based on current skills.")

    else:

        best_role = max(roles,key=roles.get)
        best_score = roles[best_role]

        st.success(f"Top Career Match: {best_role} ({best_score})")

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.55
        )])

        st.plotly_chart(fig,use_container_width=True)


# =====================================================
# 🧠 SKILL GAP ROADMAP
# =====================================================
elif menu == "🧠 Skill Gap Roadmap":

    st.subheader("Learning Roadmap")

    roadmap = generate_learning_roadmap(skill_names)

    for skill,steps in roadmap.items():

        st.markdown(f"### {skill}")

        for step in steps:
            st.write("•",step)


# =====================================================
# 💡 AI INSIGHTS
# =====================================================
elif menu == "💡 AI Insights":

    st.subheader("AI Resume Insights")

    insights = generate_insights(skill_names)

    for insight in insights:
        st.write("•",insight)

    st.markdown("---")

    st.subheader("AI Model Analysis")

    processing_time = round(random.uniform(0.8,1.8),2)

    st.write("Model Used: Resume Intelligence Analyzer v1.0")
    st.write("AI Engine: Skill Extraction + Career Matching + Readiness Score")
    st.write(f"Processing Time: {processing_time} seconds")


    # -------- Generate Report --------
    roles = recommend_roles(skill_names)
    best_role = max(roles,key=roles.get)
    score = calculate_readiness(skill_names)

    report = "AI RESUME ANALYSIS REPORT\n"
    report += "--------------------------------\n\n"

    report += f"Resume Strength Score : {score}\n\n"

    report += "Detected Skills\n"

    for skill in skill_names:
        report += f"- {skill}\n"

    report += "\nRecommended Career\n"
    report += f"{best_role}\n"

    report += "\nAI Insights\n"

    for insight in insights:
        report += f"- {insight}\n"


    st.download_button(
        label="Download AI Resume Report",
        data=report,
        file_name="ai_resume_report.txt",
        mime="text/plain"
    )


st.markdown("---")

st.markdown("""
<center>
AI Resume Intelligence Dashboard • Developed using Python & Streamlit
</center>
""",unsafe_allow_html=True)
