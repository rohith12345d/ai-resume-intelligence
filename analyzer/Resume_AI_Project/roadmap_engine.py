def generate_learning_roadmap(selected_role, user_skills):

    roadmap_db = {

        "Full Stack Developer":[
            "html","css","javascript","react","node","apis","sql"
        ],

        "Web Developer":[
            "html","css","javascript","react","bootstrap","apis"
        ],

        "Frontend Developer":[
            "html","css","javascript","react","bootstrap","ui/ux"
        ],

        "Backend Developer":[
            "python","node","sql","apis","django","flask"
        ],

        "Data Analyst":[
            "python","sql","excel","pandas","numpy","power bi","tableau"
        ],

        "Data Scientist":[
            "python","pandas","numpy","machine learning","statistics","sql"
        ],

        "Machine Learning Engineer":[
            "python","pandas","numpy","machine learning","tensorflow","pytorch"
        ],

        "AI Engineer":[
            "python","machine learning","deep learning","tensorflow","nlp"
        ],

        "DevOps Engineer":[
            "linux","docker","kubernetes","aws","ci/cd","git"
        ],

        "Software Developer":[
            "python","java","c++","data structures","algorithms","git"
        ]

    }

    required_skills = roadmap_db.get(selected_role, [])

    missing_skills= []

    for skill in required_skills:

        if skill.lower() not in [s.lower() for s in user_skills]:
            missing_skills.append(skill)

    return missing_skills
