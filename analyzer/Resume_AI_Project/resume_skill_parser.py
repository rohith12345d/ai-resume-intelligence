import re
import pdfplumber
import docx

# Skill categories

skill_categories = {

"Programming":[
"python","java","c","c++","javascript","typescript","go","rust"
],

"Web Development":[
"html","css","react","angular","vue","node","express","django","flask"
],

"Data Skills":[
"sql","mysql","postgresql","mongodb","data analysis",
"data science","data visualization","pandas","numpy","statistics"
],

"AI / Machine Learning":[
"machine learning","deep learning","tensorflow","pytorch",
"scikit-learn","nlp","computer vision"
],

"Cloud / DevOps":[
"aws","azure","gcp","docker","kubernetes","git","github","ci/cd","linux"
],

"Analytics":[
"power bi","tableau","excel"
],

"Mobile Development":[
"android","kotlin","swift","flutter"
],

"Cybersecurity":[
"cybersecurity","network security","penetration testing"
]

}


def extract_text(file):

    filename = file.name.lower()

    if filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    if filename.endswith(".pdf"):

        text = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        return text

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

    detected = {}

    for category,skills in skill_categories.items():

        found = {}

        for skill in skills:

            matches = re.findall(skill,text)

            if matches:
                found[skill] = len(matches)

        if found:
            detected[category] = found

    return detected
