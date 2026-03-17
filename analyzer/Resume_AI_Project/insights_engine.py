# insights_engine.py

def generate_insights(skills):

    insights = []
    skills = [s.lower() for s in skills]

    # -------------------------
    # STRENGTH ANALYSIS
    # -------------------------

    if "programming" in skills:
        insights.append("Your resume demonstrates solid programming capability.")

    if "web development" in skills:
        insights.append("Web development skills indicate strong frontend or full-stack potential.")

    if "data skills" in skills:
        insights.append("Data analysis skills suggest strong analytical ability.")

    if "ai / machine learning" in skills:
        insights.append("AI and Machine Learning knowledge is a strong advantage in modern tech roles.")

    if "database" in skills:
        insights.append("Database knowledge indicates good backend development capability.")

    # -------------------------
    # IMPROVEMENT SUGGESTIONS
    # -------------------------

    if "programming" not in skills:
        insights.append("Strengthen programming skills such as Python, Java or C++.")

    if "web development" not in skills:
        insights.append("Learning HTML, CSS and JavaScript can open Web Development opportunities.")

    if "backend development" not in skills:
        insights.append("Learning backend technologies like Django, Flask or Node.js will strengthen your development profile.")

    if "database" not in skills:
        insights.append("Database knowledge like SQL or MongoDB is important for most software roles.")

    if "cloud computing" not in skills:
        insights.append("Learning cloud platforms such as AWS or Azure can significantly improve employability.")

    if "devops" not in skills:
        insights.append("DevOps tools like Docker, GitHub Actions or CI/CD pipelines are valuable for modern development.")

    # -------------------------
    # CAREER ADVICE
    # -------------------------

    if len(skills) < 4:
        insights.append("Your resume currently shows limited skill diversity. Adding more technical skills will improve career opportunities.")

    if len(skills) >= 4:
        insights.append("Your resume demonstrates a balanced technical foundation.")

    insights.append("Building real-world projects and publishing them on GitHub will strengthen your profile.")

    insights.append("Adding certifications or internships can improve recruiter confidence in your skills.")

    # -------------------------
    # DEFAULT
    # -------------------------

    if len(insights) == 0:
        insights.append("Your resume shows a strong and balanced skill set. Continue improving through projects and certifications.")

    return insights
