import re

# Skill database with variations
skills_database = {
    "python": ["python", "python programming", "python developer"],
    "java": ["java", "java programming"],
    "c": ["c", "c programming"],
    "c++": ["c++"],
    "sql": ["sql", "mysql", "postgresql"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "javascript": ["javascript", "js"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "statistics": ["statistics"],
    "react": ["react", "reactjs"],
    "node": ["node", "nodejs"],
    "apis": ["api", "apis", "rest api"],
    "agile": ["agile", "agile methodology"],
    "project management": ["project management"],
    "technical writing": ["technical writing"]
}


# Extract skills from resume
def extract_skills(resume_text):

    resume_text = resume_text.lower()
    detected_skills = []

    for skill, variations in skills_database.items():

        for variation in variations:

            pattern = r"\b" + re.escape(variation) + r"\b"

            if re.search(pattern, resume_text):
                detected_skills.append(skill)
                break

    return detected_skills


# Count frequency of detected skills
def skill_frequency(resume_text, detected_skills):

    resume_text = resume_text.lower()
    frequency = {}

    for skill in detected_skills:

        variations = skills_database[skill]
        count = 0

        for variation in variations:

            pattern = r"\b" + re.escape(variation) + r"\b"
            matches = re.findall(pattern, resume_text)
            count += len(matches)

        frequency[skill] = count

    return frequency


# Check if resume mentions projects
def project_evidence(resume_text):

    resume_text = resume_text.lower()

    if "project" in resume_text:
        return True
    else:
        return False