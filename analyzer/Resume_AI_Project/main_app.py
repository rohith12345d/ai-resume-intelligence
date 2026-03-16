import streamlit as st
import pdfplumber
import docx
import time
import plotly.graph_objects as go
import plotly.express as px

from resume_skill_parser import extract_skills, skill_frequency
from career_match_engine import recommend_roles
from readiness_engine import calculate_readiness
from roadmap_engine import generate_roadmap
from insights_engine import generate_insights


st.set_page_config(page_title="AI Resume Intelligence", layout="wide")

# --------------------------
# BACKGROUND
# --------------------------

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://raw.githubusercontent.com/rohith12345d/ai-resume-intelligence/main/analyzer/Resume_AI_Project/ai_background.jpg");
            background-size: cover;
            background-position: center;
        }

        .glass{
            background: rgba(15,23,42,0.75);
            padding:20px;
            border-radius:16px;
            backdrop-filter: blur(12px);
            border:1px solid rgba(255,255,255,0.1);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# --------------------------
# HEADER
# --------------------------

st.markdown(
"""
<h1 style='text-align:center;color:#00e5ff;font-family:Inter;'>AI RESUME INTELLIGENCE SYSTEM</h1>
""",
unsafe_allow_html=True
)

st.write("Upload your resume from the sidebar to begin AI analysis.")

# --------------------------
# SIDEBAR
# --------------------------

st.sidebar.title("AI Resume System")

menu = st.sidebar.selectbox(
"Navigation",
[
"Dashboard",
"Skill Analysis",
"Career Recommendation",
"Skill Gap Roadmap",
"AI Resume Insights"
]
)

uploaded_file = st.sidebar.file_uploader(
"Upload Resume",
type=["pdf","docx"]
)

resume_text=""
skills=[]
freq={}
roles={}
readiness={}

# --------------------------
# FILE PROCESSING
# --------------------------

if uploaded_file:

    with st.spinner("Analyzing Resume with AI..."):

        if uploaded_file.type=="application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    resume_text+=page.extract_text()

        elif uploaded_file.type=="application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc=docx.Document(uploaded_file)
            for para in doc.paragraphs:
                resume_text+=para.text

        skills=extract_skills(resume_text)
        freq=skill_frequency(resume_text,skills)
        roles=recommend_roles(skills)
        readiness=calculate_readiness(skills)

# --------------------------
# DASHBOARD
# --------------------------

if menu=="Dashboard":

    if not uploaded_file:
        st.info("Upload resume to start analysis.")
    else:

        col1,col2,col3,col4=st.columns(4)

        col1.metric("Detected Skills",len(skills))
        col2.metric("Career Matches",len(roles))
        col3.metric("Projects Found","Yes" if "project" in resume_text.lower() else "No")
        col4.metric("Resume Status","Analyzed")

        score=min(len(skills)*6,100)

        fig=go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text':"AI Resume Score"},
            gauge={
                'axis':{'range':[0,100]},
                'bar':{'color':"#00e5ff"},
                'steps':[
                    {'range':[0,40],'color':'#dc2626'},
                    {'range':[40,70],'color':'#f59e0b'},
                    {'range':[70,100],'color':'#22c55e'}
                ]
            }
        ))

        st.plotly_chart(fig,use_container_width=True)

# --------------------------
# SKILL ANALYSIS
# --------------------------

if menu=="Skill Analysis":

    if not uploaded_file:
        st.warning("Upload resume first")
    else:

        df=px.data.tips()

        names=list(freq.keys())
        values=list(freq.values())

        fig=px.bar(
            x=values,
            y=names,
            orientation='h',
            color=values,
            color_continuous_scale="Blues"
        )

        st.plotly_chart(fig,use_container_width=True)

# --------------------------
# CAREER RECOMMENDATION
# --------------------------

if menu=="Career Recommendation":

    if not uploaded_file:
        st.warning("Upload resume first")
    else:

        labels=list(roles.keys())
        values=list(roles.values())

        fig=go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.4
        )])

        st.plotly_chart(fig)

# --------------------------
# SKILL GAP ROADMAP
# --------------------------

if menu=="Skill Gap Roadmap":

    if not uploaded_file:
        st.warning("Upload resume first")
    else:

        roadmap=generate_roadmap(skills)

        for skill,steps in roadmap.items():

            st.subheader(skill)

            for step in steps:
                st.write("•",step)

# --------------------------
# AI INSIGHTS
# --------------------------

if menu=="AI Resume Insights":

    if not uploaded_file:
        st.warning("Upload resume first")
    else:

        insights=generate_insights(skills,resume_text)

        for i in insights:
            st.write("•",i)
