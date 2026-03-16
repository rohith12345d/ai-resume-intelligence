# career_match_engine.py

# Job role skill database

job_roles = {

    "Data Scientist": [
        "python",
        "machine learning",
        "pandas",
        "numpy",
        "statistics",
        "data analysis"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "tensorflow",
        "pytorch",
        "deep learning"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "pandas",
        "data analysis",
        "statistics"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node"
    ],

    "Backend Developer": [
        "python",
        "java",
        "sql",
        "node"
    ]
}


def career_matches(user_skills):

    role_scores = {}

    if not user_skills:
        return {}

    for role, required_skills in job_roles.items():

        matched = 0

        for skill in required_skills:

            if skill in user_skills:
                matched += 1

        score = (matched / len(required_skills)) * 100

        role_scores[role] = round(score, 2)

    return role_scores
