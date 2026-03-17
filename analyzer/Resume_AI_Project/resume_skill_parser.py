import re
import pdfplumber
import docx

def extract_text(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text.lower()

    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = " ".join([para.text for para in doc.paragraphs])
        return text.lower()

    else:
        return uploaded_file.read().decode("utf-8").lower()


def extract_skills(uploaded_file):

    text = extract_text(uploaded_file)

    skills_db = {

        "Programming":[
            "python","c","cpp","java","javascript"
        ],

        "Web Development":[
            "html","css","javascript","react","node","bootstrap","apis"
        ],

        "Data Skills":[
            "sql","pandas","numpy","data analysis","excel"
        ],

        "AI / Machine Learning":[
            "machine learning","deep learning","tensorflow","pytorch"
        ],

        "Software Development":[
            "agile","scrum"
        ],

        "Documentation":[
            "technical writing"
        ]

    }

    detected = {}

    for category, skills in skills_db.items():

        found = []

        for skill in skills:

        # Special handling for C language
        if skill == "c":
            if re.search(r'(?<!\w)c(?!\w)', text):
                found.append(skill)
            continue
    
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found.append(skill)

        if found:
            detected[category] = found

    return detected
