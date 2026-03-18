import re
import pdfplumber
import docx


def extract_text(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        return text.lower()

    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = " ".join([p.text for p in doc.paragraphs])
        return text.lower()

    else:
        return uploaded_file.read().decode("utf-8").lower()


def extract_skills(uploaded_file):

    text = extract_text(uploaded_file)

    words = set(text.split())

    skills_db = {

        "Programming": [
            "python","java","javascript","c","cpp","c++","c#",
            "go","rust","kotlin","swift"
        ],
    
        "Web Development": [
            "html","css","react","node","apis","angular",
            "vue","bootstrap","tailwind","express"
        ],
    
        "Data Skills": [
            "sql","pandas","numpy","data analysis","data visualization",
            "excel","power bi","tableau","statistics"
        ],
    
        "AI / Machine Learning": [
            "machine learning","deep learning","tensorflow",
            "pytorch","nlp","computer vision","scikit-learn"
        ],
    
        "Project Management": [
            "agile","scrum","kanban","jira","team management"
        ],
    
        "Documentation": [
            "technical writing","documentation","report writing",
            "presentation","research writing"
        ]
    }

    detected = {}

    for category, skills in skills_db.items():

        found = []

        for skill in skills:

            if skill == "c":
                if "c" in words:
                    found.append("C")
                continue

            if " " in skill:
                if skill in text:
                    found.append(skill.title())
            else:
                if skill in words:
                    found.append(skill.title())

        if found:
            detected[category] = found

    return detected
