import streamlit as st
import plotly.graph_objects as go
import base64
import os

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
    except:
        pass

set_background()

# ---------------- TITLE ----------------
st.markdown(
"""
<h1 style='text-align:center;color:#00E5FF;font-weight:800'>
AI RESUME INTELLIGENCE DASHBOARD
</h1>
""",
unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("AI Resume Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    ["Skill Analysis", "Career Match", "Skill Gap Roadmap", "AI Insights"]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Resume",
    type=["txt", "pdf", "docx"]
)

if uploaded_file is None:
    st.info("Upload your resume from the sidebar to begin analysis")
    st.stop()

# ---------------- SKILL EXTRACTION ----------------
skills_raw = extract_skills(uploaded_file)

if not skills_raw:
    st.warning("No skills detected in resume")
    st.stop()

# -----------------------------
# AI RESUME STRENGTH METER
# -----------------------------

score = calculate_readiness(skill_names)

fig_meter = go.Figure(go.Indicator(

    mode="gauge+number",

    value=score,

    number={
        'font': {
            'size': 55,
            'color': "#00E5FF"
        }
    },

    title={
        'text': "AI Resume Strength",
        'font': {'size': 26, 'color': "#00E5FF"}
    },

    gauge={

        'axis': {
            'range': [0,100],
            'tickwidth': 2,
            'tickcolor': "#00E5FF"
        },

        'bar': {
            'color': "#00E5FF",
            'thickness': 0.35
        },

        'bgcolor': "rgba(0,0,0,0.6)",

        'borderwidth': 3,
        'bordercolor': "#00E5FF",

        'steps': [

            {'range':[0,40], 'color':"#3a0000"},
            {'range':[40,70], 'color':"#5a3a00"},
            {'range':[70,100], 'color':"#003a3a"}

        ]
    }

))

fig_meter.update_layout(

    height=350,

    paper_bgcolor="rgba(0,0,0,0)",

    font={'color':"#00E5FF"}

)

st.plotly_chart(fig_meter, use_container_width=True)

# ---- Normalize skills to dictionary ----
if isinstance(skills_raw, dict):
    skills = skills_raw
elif isinstance(skills_raw, list):
    skills = {}
    for s in skills_raw:
        skills[s] = skills.get(s, 0) + 1
else:
    skills = {}

if not skills:
    st.warning("Skill format not recognized")
    st.stop()

skill_names = list(skills.keys())
skill_values = list(skills.values())

# ---------------- RESUME SCORE ----------------
try:
    score = calculate_readiness(skills)
    if score is None:
        score = 0
except:
    score = 0

fig_meter = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={'text': "Resume Strength"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#00E5FF"},
        'steps': [
            {'range': [0, 40], 'color': "#8B0000"},
            {'range': [40, 70], 'color': "#FF8C00"},
            {'range': [70, 100], 'color': "#006400"}
        ]
    }
))
st.info(f"Total Skills Detected : {len(skill_names)}")

# ---------------- SKILL ANALYSIS ----------------
# SKILL ANALYSIS
if menu == "Skill Analysis":

    st.subheader("Detected Skills")

    # -------------------------
    # SKILL FREQUENCY BAR CHART
    # -------------------------

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
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # AI SKILL DISTRIBUTION
    # -------------------------

    st.subheader("AI Skill Distribution")

    total = sum(skill_values)

    percentages = []
    for v in skill_values:
        percent = round((v / total) * 100, 2)
        percentages.append(percent)

    fig2 = go.Figure(data=[go.Pie(
        labels=skill_names,
        values=percentages,
        hole=0.5
    )])

    fig2.update_layout(
        title="Skill Percentage Distribution",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig2, use_container_width=True)


# ---------------- CAREER MATCH ----------------
# CAREER MATCH
elif menu == "Career Match":

    st.subheader("Career Recommendation ")

    roles = recommend_roles(skill_names)

    labels = []
    values = []

    for role, score in roles.items():
        labels.append(role)
        values.append(score)

    # show best career recommendation
    best_role = max(roles, key=roles.get)
    best_score = roles[best_role]

    st.success(f"Top Career Match: {best_role} ({best_score} match score)")

    # prevent empty chart
    if sum(values) == 0:
        st.warning("No strong career match detected based on current skills.")
    else:
        fig = go.Figure(
            data=[go.Pie(
                labels=labels,
                values=values,
                hole=0.55,
                textinfo="label+percent",
                marker=dict(colors=[
                    "#00E5FF","#00FFA6","#FFD700",
                    "#FF7F50","#FF4C4C","#A29BFE",
                    "#74B9FF","#55EFC4"
                ])
            )]
        )

        fig.update_layout(
            title="AI Career Recomendation Analysis",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig, use_container_width=True)

# show best role explanation

    best_role = max(roles, key=roles.get)
    
    st.markdown("### AI Career Explanation")
    
    if best_role == "Data Scientist":
        st.write("Your resume shows strong data analysis and programming skills. These are essential for Data Science roles.")
    
    elif best_role == "Data Analyst":
        st.write("Your resume indicates good analytical and data handling skills which match Data Analyst requirements.")
    
    elif best_role == "Web Developer":
        st.write("Your resume highlights web technologies like HTML, CSS, or JavaScript which align with Web Development roles.")
    
    elif best_role == "Backend Developer":
        st.write("Your programming and database related skills are suitable for Backend Development roles.")
    
    elif best_role == "Machine Learning Engineer":
        st.write("Your resume includes machine learning or AI related skills which are required for ML Engineer roles.")
    
    elif best_role == "Full Stack Developer":
        st.write("Your resume shows both frontend and backend related skills which match Full Stack Development.")
# ---------------- SKILL GAP ROADMAP ----------------
elif menu == "Skill Gap Roadmap":

    st.subheader("Learning Roadmap")

    roadmap = generate_learning_roadmap(skill_names)

    for skill, steps in roadmap.items():
        st.markdown(f"### {skill}")
        for step in steps:
            st.write("•", step)

# ---------------- AI INSIGHTS ----------------
elif menu == "AI Insights":

    st.subheader("AI Resume Insights")

    insights = generate_insights(skill_names)

    for insight in insights:
        st.write("•", insight)
