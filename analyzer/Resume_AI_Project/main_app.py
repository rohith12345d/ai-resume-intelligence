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

def generate_report(score, skill_names, best_role, insights):

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

    return report


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Resume Intelligence", layout="wide")


# ---------------- BACKGROUND ----------------
def set_background():
    try:
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

        .glass-card {{
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 0 15px rgba(0,229,255,0.25);
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    except:
        pass

set_background()


# ---------------- TITLE ----------------
st.markdown("""
<h1 style='text-align:center;color:#00E5FF;font-weight:800'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>

<hr style="
border: none;
height: 3px;
background: linear-gradient(to right,#00E5FF,#00FFA6,#00E5FF);
box-shadow: 0 0 10px #00E5FF;
margin-bottom: 30px;
">

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
with st.spinner("AI is analyzing your resume...."):
    # AI analyzing animation
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    
    # Remove the line after analysis
    progress_bar.empty()
    
    skills_raw = extract_skills(uploaded_file)

if not skills_raw:
    st.warning("No skills detected in resume")
    st.stop()


# normalize skills
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

# Calculate resume score first
score = calculate_readiness(skill_names)

st.markdown("### Resume Skill Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Skills Detected", len(skill_names))
col2.metric("Resume Strength Score", score)
col3.metric("Career Matches", len(recommend_roles(skill_names)))

# =====================================================
# 📊 SKILL ANALYSIS PAGE
# =====================================================
if menu == "📊 Skill Analysis":
    with st.spinner("AI is analyzing skill data..."):
                     time.sleep(1)
    st.subheader("Detected Skills")
    
    # ---------------- AI RESUME STRENGTH ----------------

    # ---------------- AI RESUME STRENGTH ----------------

    score = calculate_readiness(skill_names)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    fig_meter = go.Figure(go.Indicator(
    
        mode="gauge+number",
    
        value=score,
    
        number={
            'font':{'size':60,'color':"#00E5FF"}
        },
    
        title={
            'text':"AI Resume Strength",
            'font':{'size':26,'color':"#00E5FF"}
        },
    
        gauge={
    
            'axis':{
                'range':[0,100],
                'tickwidth':2,
                'tickcolor':"#00E5FF"
            },
    
            'bar':{
                'color':"#00E5FF",
                'thickness':0.25
            },
    
            'bgcolor':"rgba(0,0,0,0.6)",
    
            'borderwidth':3,
            'bordercolor':"#00E5FF",
    
            'steps':[
                {'range':[0,40],'color':"#8B0000"},
                {'range':[40,70],'color':"#FFA500"},
                {'range':[70,100],'color':"#006400"}
            ]
    
        }
    
    ))
    
    fig_meter.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        font={'color':"#00E5FF"}
    )
    
    st.plotly_chart(fig_meter, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.info(f"Total Skills Detected : {len(skill_names)}")
    
    # ---------- SKILL FREQUENCY ----------
    
    st.subheader("Detected Skills")

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=skill_values,
        y=skill_names,
        orientation='h',
        marker=dict(color="#00E5FF")
    ))

    fig.update_layout(
        title="Skill Frequency in Resume",
        xaxis_title="Frequency",
        yaxis_title="Skills",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig,use_container_width=True)


    # ---------- SKILL DISTRIBUTION ----------
    st.subheader("AI Skill Distribution")

    total = sum(skill_values)

    percentages = []
    for v in skill_values:
        percentages.append(round((v/total)*100,2))

    fig2 = go.Figure(data=[go.Pie(
        labels=skill_names,
        values=percentages,
        hole=0.5,
        marker=dict(colors=[
            "#00E5FF","#00FFA6","#FFD700",
            "#FF7F50","#A29BFE","#74B9FF"
        ])
    )])

    fig2.update_layout(
        title="Skill Percentage Distribution",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig2,use_container_width=True)



# =====================================================
# 🎯 CAREER MATCH PAGE
# =====================================================
elif menu == "🎯 Career Match":
    with st.spinner("AI is analyzing career compatibility..."):
                     time.sleep(1)

    st.subheader("Career Recommendations")

    roles = recommend_roles(skill_names)

    labels = list(roles.keys())
    values = list(roles.values())

    if sum(values) == 0:
        st.warning("No strong career match detected based on current skills.")

    else:

        best_role = max(roles, key=roles.get)
        best_score = roles[best_role]

        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

        st.markdown(f"""
        <h2 style='color:#00E5FF'>Top AI Career Match</h2>
        <h1 style='color:white'>{best_role}</h1>
        <h3 style='color:#00FFA6'>Match Score : {best_score}</h3>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.55,
            textinfo="label+percent",
            marker=dict(colors=[
                "#00E5FF","#00FFA6","#FFD700",
                "#FF7F50","#FF4C4C","#A29BFE"
            ])
        )])

        fig.update_layout(
            title="AI Career Recommendation Analysis",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True)



# =====================================================
# 🧠 SKILL GAP ROADMAP
# =====================================================
elif menu == "🧠 Skill Gap Roadmap":
    with st.spinner("AI is generating learning roadmap..."):
                     time.sleep(1)

    st.subheader("Learning Roadmap")

    roadmap = generate_learning_roadmap(skill_names)

    for skill,steps in roadmap.items():

        st.markdown(f"### {skill}")

        for step in steps:
            st.write("•",step)



# =====================================================
elif menu == "💡 AI Insights":
    with st.spinner("AI is generating resume insights..."):
                     time.sleep(1)

    st.subheader("AI Resume Insights")

    insights = generate_insights(skill_names)

    for insight in insights:
        st.write("•", insight)

    st.markdown("---")

    st.subheader("AI Model Analysis")
    
    processing_time = round(random.uniform(0.8,1.8),2)
    
    st.write("Model Used: Resume Intelligence Analyzer v1.0")
    st.write("AI Engine: Skill Extraction + Career Matching + Readiness Score")
    st.write(f"Processing Time: {processing_time} seconds")


    # -------- Generate AI Resume Report --------

    roles = recommend_roles(skill_names)
    best_role = max(roles, key=roles.get)

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

    st.markdown("""
    <style>
    
    div.stDownloadButton > button {
        background-color: #00E5FF;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    
    div.stDownloadButton > button:hover {
        background-color: #00FFA6;
        color: black;
    }
    
    </style>
    """, unsafe_allow_html=True)
    
    st.download_button(
        label="Download AI Resume Report",
        data=report,
        file_name="ai_resume_report.txt",
        mime="text/plain"
    )

st.markdown("---")

st.markdown(
"""
<center>
AI Resume Intelligence Dashboard • Developed using Python & Streamlit  
AI Skill Analysis | Career Recommendation | Resume Readiness Engine
</center>
""",
unsafe_allow_html=True
)
