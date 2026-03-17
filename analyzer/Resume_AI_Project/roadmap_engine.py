# roadmap_engine.py
def generate_learning_roadmap(selected_role, skill_names):

    roadmap = {}

    if selected_role == "Full Stack Developer":

        required_skills = ["html","css","javascript","react","node"]

        missing = []

        for skill in required_skills:

            if skill not in skill_names:
                missing.append(skill)

        roadmap["Skills to Learn"] = missing

    return roadmap

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

        if skill not in skill_names:
            roadmap[skill] = steps

    return roadmap
