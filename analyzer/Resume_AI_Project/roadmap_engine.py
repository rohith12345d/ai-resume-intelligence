# roadmap_engine.py

def generate_learning_roadmap(selected_role,skill_names):

    roadmap = {}

    learning_paths = {

        "python": [
            "Learn Python Basics",
            "Understand OOP Concepts",
            "Practice Data Structures",
            "Build Python Projects"
        ],

        "machine learning": [
            "Learn Supervised Learning",
            "Study Regression & Classification",
            "Understand Model Evaluation",
            "Build ML Projects"
        ],

        "sql": [
            "Learn SQL Basics",
            "Practice Joins",
            "Learn Aggregations",
            "Work with Databases"
        ],

        "data analysis": [
            "Learn Pandas",
            "Practice Data Cleaning",
            "Perform Exploratory Data Analysis",
            "Create Data Visualizations"
        ],

        "deep learning": [
            "Understand Neural Networks",
            "Learn TensorFlow or PyTorch",
            "Practice Image / Text Models",
            "Build Deep Learning Projects"
        ]
    }

    for skill, steps in learning_paths.items():

        if skill not in user_skills:
            roadmap[skill] = steps

    return roadmap
