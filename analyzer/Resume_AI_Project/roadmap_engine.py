def generate_learning_roadmap(selected_role, user_skills):

    roadmap_db = {

        "Full Stack Developer":[
            "html","css","javascript","react","node","apis","sql"
        ],

        "Data Scientist":[
            "python","pandas","numpy","machine learning","sql"
        ],

        "Machine Learning Engineer":[
            "python","pandas","numpy","machine learning","tensorflow"
        ]

    }

    required = roadmap_db.get(selected_role, [])

    missing = []

    for skill in required:
        if skill not in user_skills:
            missing.append(skill)

    return missing
