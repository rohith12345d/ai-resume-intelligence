# resume_skill_parser.py

import re

skill_database = [
    "python",
    "machine learning",
    "data analysis",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "pandas",
    "numpy"
]


def extract_skills(uploaded_file):

    text = uploaded_file.read().decode("utf-8", errors="ignore")
    text = text.lower()

    skill_counts = {}

    for skill in skill_database:

        count = len(re.findall(skill, text))

        if count > 0:
            skill_counts[skill] = count

    return skill_counts
