# resume_skill_parser.py

import io

def extract_skills(uploaded_file):

    text = ""

    # detect file type
    file_name = uploaded_file.name.lower()

    # ---------- TXT ----------
    if file_name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")

    # ---------- PDF ----------
    elif file_name.endswith(".pdf"):
        import PyPDF2
        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    # ---------- DOCX ----------
    elif file_name.endswith(".docx"):
        import docx
        doc = docx.Document(uploaded_file)

        for para in doc.paragraphs:
            text += para.text

    text = text.lower()

    # -----------------------
    # SKILL DATABASE
    # -----------------------

    skills_db = {

        "Programming": [
        "python","c","cpp","java","javascript"
        ],
        
        "Web Development": [
        "html","css","javascript","react","node","apis"
        ],
        
        "Data Skills": [
        "sql","pandas","numpy","data analysis","excel"
        ],
        
        "AI / Machine Learning": [
        "machine learning","deep learning","tensorflow","pytorch","scikit-learn"
        ],
        
        "Software Development": [
        "agile","agile project management"
        ],
        
        "Documentation": [
        "technical writing"
        ]
        
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
