def generate_roadmap(skills):

    roadmap={}

    if "python" not in skills:
        roadmap["Python"]=[
        "Python Basics",
        "OOP Concepts",
        "Data Structures",
        "NumPy & Pandas",
        "Machine Learning Libraries"
        ]

    if "machine learning" not in skills:
        roadmap["Machine Learning"]=[
        "Supervised Learning",
        "Regression & Classification",
        "Model Evaluation",
        "Scikit Learn",
        "ML Projects"
        ]

    if "sql" not in skills:
        roadmap["SQL"]=[
        "Basic Queries",
        "Joins",
        "Aggregations",
        "Database Design"
        ]

    return roadmap
