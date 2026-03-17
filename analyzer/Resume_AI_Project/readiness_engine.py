# readiness_engine.py

def calculate_readiness(skills):

    if not skills:
        return 0

    # total skills detected
    total_skills = len(skills)

    # simple readiness scoring
    if total_skills >= 10:
        score = 90
    elif total_skills >= 7:
        score = 75
    elif total_skills >= 5:
        score = 60
    elif total_skills >= 3:
        score = 40
    else:
        score = 20

    return score
