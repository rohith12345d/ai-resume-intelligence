import re
import pdfplumber
import docx

# Skill database
skills_db = [
    "python",
    "machine learning",
    "deep learning",
    "data analysis",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch"
]


def extract_text(file):

    filename = file.name.lower()

    # TXT FILE
    if filename.endswith(".txt"):
        return file.read().decode("utf-8")

    # PDF FILE
    if filename.endswith(".pdf"):

        text = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        return text

    # DOCX FILE
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
