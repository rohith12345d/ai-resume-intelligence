# career_match_engine.py

# Job role skill database
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
        "node"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "data analysis",
        "pandas",
        "statistics"
    ]
}


def recommend_roles(user_skills):

    role_scores = {}

    for role, required_skills in job_roles.items():

        matched = 0

        for skill in required_skills:
            if skill in user_skills:
                matched += 1

        score = (matched / len(required_skills)) * 100

        role_scores[role] = round(score, 2)

    return role_scores