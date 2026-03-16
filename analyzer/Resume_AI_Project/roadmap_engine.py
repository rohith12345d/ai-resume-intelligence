# roadmap_engine.py

def generate_learning_roadmap(skills):

    roadmap = {}

    skill_paths = {

        "python": [
            "Python Basics",
            "OOP Concepts",
            "Data Structures in Python",
            "Python Projects"
        ],

        "machine learning": [
            "Linear Regression",
            "Classification Algorithms",
            "Model Evaluation",
            "ML Projects"
        ],

        "sql": [
            "SQL Basics",
            "Joins",
            "Aggregation",
            "Database Projects"
        ],

        "data analysis": [
            "Pandas",
            "Data Cleaning",
            "Visualization",
            "EDA Projects"
        ]
    }

    for skill in skill_paths:

        if skill not in skills:
            roadmap[skill] = skill_paths[skill]

    return roadmap
