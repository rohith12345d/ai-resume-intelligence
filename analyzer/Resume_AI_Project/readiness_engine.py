# readiness_engine.py

def calculate_readiness(skill_names):

    if not skill_names:
        return 0

    skill_count = len(skill_names)

    # simple scoring logic
    if skill_count <= 2:
        return 25
    elif skill_count <= 4:
        return 40
    elif skill_count <= 6:
        return 60
    elif skill_count <= 8:
        return 75
    elif skill_count <= 10:
        return 85
    else:
        return 95
