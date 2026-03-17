import re
import pdfplumber
import docx

def extract_skills(uploaded_file):

    text = ""

    # READ TXT FILE
    if uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8", errors="ignore")

    # READ PDF FILE
    elif uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

    # READ DOCX FILE
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    text = text.lower()
    print(text)

    skills_db = {

    "Programming":[
    "python","c","cpp","java","javascript","go","rust","typescript"
    ],

    "Web Development":[
    "html","css","javascript","react","node","django","flask","bootstrap","apis"
    ],

    "Data Skills":[
    "sql","pandas","numpy","data analysis","excel","power bi","tableau"
    ],

    "AI / Machine Learning":[
    "machine learning","deep learning","tensorflow","pytorch","scikit-learn","nlp"
    ],

    "Cloud / DevOps":[
    "aws","docker","kubernetes","git","github","ci/cd"
    ],

    "Software Development":[
    "agile","agile project management","scrum"
    ],

    "Documentation":[
    "technical writing","documentation"
    ]

    }

    detected = {}

    for category, skills in skills_db.items():
        found_skills = []

        for skill in skills :

            if re.search(r'\b'+re.escape(skill)+r'\b', text):
                found_skills.append(skill)
        if found_skills:
            detected[category] = found_skills

    return detected
