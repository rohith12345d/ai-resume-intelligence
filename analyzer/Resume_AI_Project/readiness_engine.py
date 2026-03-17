# resume_skill_parser.py

import pdfplumber
import docx
import calculate_readiness

def extract_skills(uploaded_file):

    text = ""
    file_name = uploaded_file.name.lower()

    # -------- TXT --------
    if file_name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")

    # -------- PDF --------
    elif file_name.endswith(".pdf"):

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

    # -------- DOCX --------
    elif file_name.endswith(".docx"):

        doc = docx.Document(uploaded_file)

        for para in doc.paragraphs:
            text += para.text

    text = text.lower()

    # ---------------------
    # SKILL DATABASE
    # ---------------------

    skills_db = {
        "Programming": ["python","java","c++","javascript"],
        "Web Development": ["html","css","react","node","django"],
        "Data Skills": ["sql","pandas","numpy","data analysis"],
        "AI / Machine Learning": ["machine learning","deep learning","tensorflow","keras","scikit"]
    }

    detected = {}

    for category, skill_list in skills_db.items():

        count = 0

        for skill in skill_list:
            if skill in text:
                count += 1

        if count > 0:
            detected[category] = count

    return detected
