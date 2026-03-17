import re
import pdfplumber
import docx
def extract_skills(uploaded_file):

    text = uploaded_file.read().decode("utf-8").lower()

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

        count = 0

        for skill in skills:

            if re.search(r'\b'+re.escape(skill)+r'\b', text):
                count += 1

        if count > 0:
            detected[category] = count

    return detected
