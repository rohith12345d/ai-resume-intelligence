import streamlit as st
import pdfplumber
import docx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time
import base64

from resume_skill_parser import extract_skills
from resume_skill_parser import skill_frequency
from resume_skill_parser import project_evidence
from career_match_engine import recommend_roles
from readiness_engine import calculate_readiness


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="AI Resume Intelligence",
    page_icon="🤖",
    layout="wide"
)


# ------------------------------------------------
# BACKGROUND IMAGE
# ------------------------------------------------

def set_background():
   with open("analyzer/Resume_AI_Project/ai_background.jpg","rb") as img:
        encoded = base64.b64encode(img.read()).decode()

   st.markdown(
        f"""
        <style>

        .stApp {{
        background-image:
    linear-gradient(rgba(2,6,23,0.55), rgba(2,6,23,0.55))    
        url("data:image/jpg;base64,{encoded}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background()


# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

st.sidebar.title("🤖 AI Resume System")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Skill Analysis",
        "Career Recommendation",
        "Skill Gap & Roadmap"
    ]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Resume",
    type=["txt","pdf","docx"]
)


resume_text=""
skills=[]
frequency={}
role_scores={}
readiness_scores={}
project_found=False


# ------------------------------------------------
# AI ANALYSIS PROGRESS
# ------------------------------------------------

if uploaded_file is not None:

    progress_text = st.empty()
    progress_bar = st.progress(0)

    progress_text.text("Uploading Resume...")
    progress_bar.progress(20)
    time.sleep(0.5)

    if uploaded_file.type == "text/plain":
        resume_text = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    resume_text += text

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            resume_text += para.text


    progress_text.text("Extracting Skills...")
    progress_bar.progress(40)
    time.sleep(0.5)

    skills = extract_skills(resume_text)


    progress_text.text("Analyzing Skill Frequency...")
    progress_bar.progress(60)
    time.sleep(0.5)

    frequency = skill_frequency(resume_text, skills)


    progress_text.text("Generating Career Recommendations...")
    progress_bar.progress(80)
    time.sleep(0.5)

    role_scores = recommend_roles(skills)
    readiness_scores = calculate_readiness(skills)
    project_found = project_evidence(resume_text)


    progress_text.text("Finalizing AI Analysis...")
    progress_bar.progress(100)
    time.sleep(0.5)

    progress_text.empty()
    progress_bar.empty()



# ------------------------------------------------
# DASHBOARD
# ------------------------------------------------

if menu=="Dashboard":

    st.title("AI Resume Intelligence Dashboard")

    if uploaded_file is None:

        st.info("Upload your resume from the sidebar to begin analysis.")

    else:

        col1,col2,col3,col4 = st.columns(4)

        col1.metric("Detected Skills",len(skills))
        col2.metric("Career Matches",len(role_scores))
        col3.metric("Projects Found","Yes" if project_found else "No")
        col4.metric("Resume Status","Analyzed")


        # --------------------------------
        # AI RESUME SCORE GAUGE
        # --------------------------------

        resume_score = min(len(skills) * 6, 100)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=resume_score,
            title={'text': "AI Resume Score"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "#22d3ee"},
                'steps': [
                    {'range': [0,40], 'color': "#dc2626"},
                    {'range': [40,70], 'color': "#f59e0b"},
                    {'range': [70,100], 'color': "#22c55e"}
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)



# ------------------------------------------------
# SKILL ANALYSIS
# ------------------------------------------------

if menu=="Skill Analysis":

    st.title("Skill Analysis")

    if uploaded_file is None:

        st.warning("Upload resume first.")

    else:

        st.subheader("Detected Skills")

        cols = st.columns(4)

        for i, skill in enumerate(skills):

            cols[i % 4].markdown(
                f"""
                <div style="
                background: rgba(30,41,59,0.7);
                padding:12px;
                border-radius:10px;
                text-align:center;
                color:#38bdf8;
                font-weight:500;">
                {skill.upper()}
                </div>
                """,
                unsafe_allow_html=True
            )


        st.subheader("Skill Strength")

        skills_list = list(frequency.keys())
        values = list(frequency.values())

        fig, ax = plt.subplots()

        ax.bar(
            skills_list,
            values,
            color=["#38bdf8","#60a5fa","#22d3ee","#818cf8","#f472b6"]
        )

        ax.set_facecolor("black")
        fig.set_facecolor("black")

        ax.tick_params(colors="white")

        plt.xticks(rotation=45)

        st.pyplot(fig)



# ------------------------------------------------
# CAREER RECOMMENDATION
# ------------------------------------------------

if menu=="Career Recommendation":

    st.title("Career Recommendation")

    if uploaded_file is None:

        st.warning("Upload resume first.")

    else:

        roles=list(role_scores.keys())
        scores=list(role_scores.values())

        fig, ax = plt.subplots()

        colors=[
            "#38bdf8",
            "#22d3ee",
            "#818cf8",
            "#f472b6",
            "#34d399"
        ]

        ax.pie(
            scores,
            labels=roles,
            autopct="%1.1f%%",
            colors=colors,
            startangle=90
        )

        ax.axis("equal")

        st.pyplot(fig)


        st.subheader("Career Readiness")

        for role, score in readiness_scores.items():

            st.write(role)

            st.progress(int(score))

            st.write(str(score) + "% readiness")



# ------------------------------------------------
# SKILL GAP ANALYSIS
# ------------------------------------------------

if menu=="Skill Gap & Roadmap":

    st.title("Skill Gap Analysis & Learning Roadmap")

    if uploaded_file is None:

        st.warning("Upload resume first.")

    else:

        job_roles = {

        "Data Scientist":["python","machine learning","statistics","pandas","numpy","data analysis"],
        "Machine Learning Engineer":["python","machine learning","tensorflow","pytorch","numpy"],
        "AI Engineer":["python","machine learning","deep learning","tensorflow","pytorch"],
        "Data Analyst":["python","sql","data analysis","pandas","statistics"],
        "Backend Developer":["python","java","sql","apis","node"],
        "Frontend Developer":["html","css","javascript","react"],
        "Web Developer":["html","css","javascript","react","node"],
        "Full Stack Developer":["html","css","javascript","react","node","sql"],
        "Software Engineer":["python","java","c","algorithms","data structures"],
        "DevOps Engineer":["linux","docker","kubernetes","python","cloud"],
        "Cloud Engineer":["aws","cloud","docker","linux","python"]

        }

        selected_role = st.selectbox(
            "Select Target Role",
            list(job_roles.keys())
        )

        required_skills = job_roles[selected_role]

        missing_skills=[]

        for skill in required_skills:

            if skill not in skills:
                missing_skills.append(skill)


        if missing_skills:

            st.subheader("Missing Skills")

            missing_html=""

            for skill in missing_skills:

                missing_html += f"""
                <span style="
                background:#dc2626;
                padding:8px 16px;
                border-radius:20px;
                margin:6px;
                display:inline-block;
                color:white;">
                {skill.upper()}
                </span>
                """

            st.markdown(missing_html,unsafe_allow_html=True)


            st.subheader("Learning Roadmap")

            for i, skill in enumerate(missing_skills, start=1):

                st.write(f"Step {i}: Learn {skill}")

        else:

            st.success("You already meet the requirements for this role.")
