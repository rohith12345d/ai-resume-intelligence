# career_match_engine.py

def recommend_roles(user_skills):

    # expand category skills
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
            if skill in expanded_skills:
                matched += 1

        score = matched   # use raw match count

        if score > 0:
            role_scores[role] = score

    # sort roles by best match
    role_scores = dict(sorted(role_scores.items(), key=lambda x: x[1], reverse=True))
    role_scores = dict(list(role_scores.items())[:4])

    return role_scores
