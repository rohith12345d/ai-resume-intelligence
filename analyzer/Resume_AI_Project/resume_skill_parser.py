import pdfplumber
import docx


def extract_text_from_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text


def extract_text_from_docx(file):

    doc = docx.Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text

    return text


def extract_skills(uploaded_file):

    if uploaded_file is None:
        return []

    file_type = uploaded_file.name.split(".")[-1].lower()

    resume_text = ""

    if file_type == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)

    elif file_type == "docx":
        resume_text = extract_text_from_docx(uploaded_file)

    else:
        resume_text = uploaded_file.read().decode("utf-8", errors="ignore")

    if not resume_text:
        return []

    resume_text = resume_text.lower()

    skill_database = [
        "python",
        "machine learning",
        "data analysis",
        "sql",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "pandas",
        "numpy",
        "statistics"
    ]

    found_skills = []

    for skill in skill_database:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills
