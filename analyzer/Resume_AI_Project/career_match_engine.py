# career_match_engine.py

def recommend_roles(user_skills):

    job_roles = {

    "Data Scientist": [
        "python","machine learning","pandas","numpy","statistics","data analysis"
    ],

    "Data Analyst": [
        "python","sql","excel","pandas","data analysis","statistics"
    ],

    "Machine Learning Engineer": [
        "python","machine learning","tensorflow","pytorch","deep learning"
    ],

    "AI Engineer": [
        "python","machine learning","deep learning","tensorflow","keras"
    ],

    "Web Developer": [
        "html","css","javascript","react","node","bootstrap"
    ],

    "Frontend Developer": [
        "html","css","javascript","react","angular"
    ],

    "Backend Developer": [
        "python","java","sql","node","django","flask"
    ],

    "Full Stack Developer": [
        "html","css","javascript","react","node","sql"
    ],

    "Software Engineer": [
        "python","java","c++","data structures","algorithms"
    ],

    "DevOps Engineer": [
        "docker","kubernetes","aws","linux","ci/cd"
    ],

    "Cloud Engineer": [
        "aws","azure","cloud","docker","kubernetes"
    ],

    "Cybersecurity Analyst": [
        "network security","cryptography","ethical hacking","linux"
    ],

    "Mobile App Developer": [
        "flutter","android","java","kotlin","react native"
    ]

}

    role_scores = {}

    for role, required_skills in job_roles.items():

        matched = 0

        for skill in required_skills:

            if skill.lower() in [s.lower() for s in user_skills]:
                matched += 1

        score = (matched / len(required_skills)) * 100

        role_scores[role] = round(score, 2)

    return role_scores
