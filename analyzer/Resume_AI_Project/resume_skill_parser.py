import pdfplumber
import docx


# skill database

skill_database = [
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
    "statistics",
    "tensorflow",
    "pytorch",
    "nlp"
]


# extract text from pdf

def extract_text_from_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


# extract text from docx

def extract_text_from_docx(file):

    doc = docx.Document(file)

    text = ""

    for para in doc.paragraphs:

        text += para.text + " "

    return text


# main function

def extract_skills(uploaded_file):

    if uploaded_file is None:
        return []

    file_type = uploaded_file.name.split(".")[-1].lower()

    resume_text = ""

    try:

        if file_type == "pdf":

            resume_text = extract_text_from_pdf(uploaded_file)

        elif file_type == "docx":

            resume_text = extract_text_from_docx(uploaded_file)

        elif file_type == "txt":

            resume_text = uploaded_file.read().decode("utf-8")

        else:

            return []

    except:
        return []

    resume_text = resume_text.lower()

    found_skills = []

    for skill in skill_database:

        if skill in resume_text:

            found_skills.append(skill)

    return found_skills
