# readiness_engine.py

job_roles = {
    "Data Scientist": [
        "python",
        "machine learning",
        "statistics",
        "pandas",
        "numpy",
        "data analysis"
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
        "apis"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "data analysis",
        "pandas"
    ]
}


def calculate_readiness(user_skills):

    readiness_scores = {}

    for role, required_skills in job_roles.items():

        matched = 0

        for skill in required_skills:
            if skill in user_skills:
                matched += 1

        score = (matched / len(required_skills)) * 100

        readiness_scores[role] = round(score, 2)

    return readiness_scores