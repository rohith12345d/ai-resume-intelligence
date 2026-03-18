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
        text = " ".join([p.text for p in doc.paragraphs])
        return text.lower()

    else:
        return uploaded_file.read().decode("utf-8").lower()


def extract_skills(uploaded_file):

    text = extract_text(uploaded_file)

    skills_db = {
        "Programming":["python","java","javascript","c","cpp"],
        "Web Development":["html","css","react","node","apis"],
        "Data Skills":["sql","pandas","numpy","data analysis"],
        "AI / Machine Learning":["machine learning"],
        "Project Management":["agile"],
        "Documentation":["technical writing"]
    }

    detected = {}

    for category, skills in skills_db.items():

        found = []

        for skill in skills:

            if skill == "c":
                if re.search(r'(?<![a-zA-Z])c(?![a-zA-Z])', text):
                    found.append("C")
                continue

            if re.search(r'\b' + re.escape(skill) + r'\b', text):
                found.append(skill.title())
        if found:
            detected[category] = found

    return detected
