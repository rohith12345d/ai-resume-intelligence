import re
import pdfplumber
import docx


# ---------------- TEXT EXTRACTION ----------------

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


# ---------------- SKILL EXTRACTION ----------------

def extract_skills(uploaded_file):

    text = extract_text(uploaded_file)

    skills_db = {

        "Programming":[
            "python","c","cpp","java","javascript","typescript",
            "go","rust","ruby","php","swift","kotlin","scala","r","matlab"
        ],

        "Web Development":[
            "html","css","javascript","react","angular","vue",
            "node","express","django","flask","spring","bootstrap",
            "tailwind","apis","rest api","graphql","jquery"
        ],

        "Data Skills":[
            "sql","mysql","postgresql","mongodb",
            "pandas","numpy","data analysis","data visualization",
            "excel","power bi","tableau","statistics"
        ],

        "AI / Machine Learning":[
            "machine learning","deep learning","tensorflow","pytorch",
            "scikit-learn","nlp","computer vision","neural networks",
            "transformers","reinforcement learning"
        ],

        "Cloud / DevOps":[
            "aws","azure","google cloud","gcp",
            "docker","kubernetes","terraform","jenkins",
            "ci/cd","devops","linux","bash"
        ],

        "Database":[
            "mysql","postgresql","mongodb","redis",
            "firebase","cassandra","dynamodb","sqlite"
        ],

        "Mobile Development":[
            "android","ios","flutter","react native",
            "swift","kotlin"
        ],

        "Cybersecurity":[
            "cybersecurity","ethical hacking",
            "penetration testing","network security",
            "cryptography","kali linux"
        ],

        "Software Development":[
            "software engineering","oop","object oriented programming",
            "design patterns","system design","microservices"
        ],

        "Project Management":[
            "agile","scrum","kanban","jira",
            "project management","product management"
        ],

        "Documentation":[
            "technical writing","documentation",
            "requirement analysis"
        ],

        "Tools":[
            "git","github","gitlab","bitbucket",
            "vscode","intellij","eclipse",
            "figma","postman"
        ]
    }

    detected = {}

    for category, skills in skills_db.items():

        found = []

        for skill in skills:

            # Special handling for C language
            if skill == "C":
                if re.search(r'(?<![a-zA-Z])c(?![a-zA-Z])', text):
                    found.append("c")
                continue

            if re.search(r'\b' + re.escape(skill) + r'\b', text):
                found.append(skill)

        if found:
            detected[category] = found

    return detected
