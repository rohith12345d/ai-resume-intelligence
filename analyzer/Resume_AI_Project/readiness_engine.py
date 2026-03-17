# readiness_engine.py

def calculate_readiness(skill_names):

    if not skill_names:
        return 0

    skill_count = len(skill_names)

    # simple scoring logic
    if skill_count >= 10:
        return 90
    elif skill_count >= 7:
        return 75
    elif skill_count >= 5:
        return 60
    elif skill_count >= 3:
        return 40
    else:
        return 20
