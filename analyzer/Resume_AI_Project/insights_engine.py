# insights_engine.py

def generate_insights(skills):

    insights = []

    skill_set = [s.lower() for s in skills]

    if "programming" not in skill_set:
        insights.append("Improve programming skills such as Python or Java.")

    if "data skills" not in skill_set:
        insights.append("Learning SQL, Pandas, and Data Analysis will improve your profile.")

    if "web development" not in skill_set:
        insights.append("Consider learning HTML, CSS, and JavaScript to expand your opportunities.")

    if "ai / machine learning" not in skill_set:
        insights.append("Machine Learning knowledge can significantly increase career opportunities.")

    if len(skills) < 4:
        insights.append("Adding more technical skills to your resume will improve your readiness score.")

    if not insights:
        insights.append("Your resume shows a strong skill set. Continue building projects to strengthen your profile.")

    return insights
