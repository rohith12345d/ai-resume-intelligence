# readiness_engine.py
def calculate_readiness(skills):

    if not skills:
        return 0

    important_skills = [
        "python",
        "machine learning",
        "sql",
        "data analysis",
        "pandas",
        "statistics"
    ]

    matched = 0

    for skill in skills:
        if skill in important_skills:
            matched += 1

    score = (matched / len(important_skills)) * 100

    return round(score)
