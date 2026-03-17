# career_match_engine.py

def recommend_roles(user_skills):

    # convert skill categories into real skills
    expanded_skills = []

    for skill in user_skills:

        if skill == "Programming":
            expanded_skills += ["python","java","c++","javascript"]

        elif skill == "Web Development":
            expanded_skills += ["html","css","react","node"]

        elif skill == "Data Skills":
            expanded_skills += ["sql","pandas","numpy","data analysis"]

        elif skill == "AI / Machine Learning":
            expanded_skills += ["machine learning","tensorflow","keras"]

        else:
            expanded_skills.append(skill)

    job_roles = {

        "Data Scientist":[
            "python","machine learning","pandas","numpy","data analysis"
        ],

        "Data Analyst":[
            "python","sql","pandas","data analysis"
        ],

        "Web Developer":[
            "html","css","javascript","react"
        ],

        "Backend Developer":[
            "python","java","sql","node"
        ],

        "Machine Learning Engineer":[
            "python","machine learning","tensorflow","keras"
        ],

        "Full Stack Developer":[
            "html","css","javascript","react","node","sql"
        ]

    }

    role_scores = {}

    for role, required_skills in job_roles.items():

        matched = 0

        for skill in required_skills:

            if skill.lower() in [s.lower() for s in expanded_skills]:
                matched += 1

        score = (matched / len(required_skills)) * 100
        role_scores[role] = round(score,2)

    return role_scores
