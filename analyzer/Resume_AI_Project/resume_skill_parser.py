# resume_skill_parser.py

def extract_skills(uploaded_file):

    try:
        text = uploaded_file.read().decode("utf-8").lower()
    except:
        text = str(uploaded_file.read()).lower()

    skills_db = {
        "Programming": ["python","java","c++","c","javascript"],
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
