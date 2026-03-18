def extract_skills(uploaded_file):

    text = extract_text(uploaded_file)

    # Split resume text into words
    words = set(text.split())

    skills_db = {
        "Programming": ["python","java","javascript","c","cpp"],
        "Web Development": ["html","css","react","node","apis"],
        "Data Skills": ["sql","pandas","numpy","data analysis"],
        "AI / Machine Learning": ["machine learning"],
        "Project Management": ["agile"],
        "Documentation": ["technical writing"]
    }

    detected = {}

    for category, skills in skills_db.items():

        found = []

        for skill in skills:

            # Special case for C language
            if skill == "c":
                if "c" in words:
                    found.append("C")
                continue

            # Handle multi-word skills
            if " " in skill:
                if skill in text:
                    found.append(skill.title())

            else:
                if skill in words:
                    found.append(skill.title())

        if found:
            detected[category] = found

    return detected
