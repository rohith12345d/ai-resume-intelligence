import re
import pdfplumber
import docx

# Large AI Skill Database (can be expanded anytime)

skills_db = [

# Programming
"python","java","c","c++","javascript","typescript","go","rust",

# Web
"html","css","react","angular","vue","node","express","django","flask",

# Data
"sql","mysql","postgresql","mongodb","data analysis","data science",
"data visualization","pandas","numpy","statistics",

# AI / ML
"machine learning","deep learning","tensorflow","pytorch",
"scikit-learn","nlp","computer vision",

# Cloud
"aws","azure","gcp","docker","kubernetes",

# DevOps
"git","github","ci/cd","linux","bash",

# Analytics
"power bi","tableau","excel",

# Mobile
"android","kotlin","swift","flutter",

# Security
"cybersecurity","network security","penetration testing"
]


def extract_text(file):

    filename = file.name.lower()

    # TXT
    if filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    # PDF
    if filename.endswith(".pdf"):

        text = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        return text

    # DOCX
    if filename.endswith(".docx"):

        doc = docx.Document(file)

        text = ""

        for para in doc.paragraphs:
            text += para.text + " "

        return text

    return ""


def extract_skills(uploaded_file):

    text = extract_text(uploaded_file)

    text = text.lower()

    skill_counts = {}

    for skill in skills_db:

        matches = re.findall(skill, text)

        if matches:
            skill_counts[skill] = len(matches)

    return skill_counts
