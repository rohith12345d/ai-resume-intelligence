# insights_engine.py

def generate_insights(skills):

    insights = []

    if not skills:
        insights.append("No skills detected in the resume.")
        insights.append("Try uploading a clearer resume.")
        return insights

    insights.append(f"{len(skills)} technical skills detected in your resume.")

    if "python" in skills:
        insights.append("Python detected — strong skill for data and AI roles.")

    if "machine learning" in skills:
        insights.append("Machine Learning detected — suitable for AI Engineer roles.")

    if "sql" not in skills:
        insights.append("Learning SQL can improve your chances for data-related roles.")

    if "data analysis" not in skills:
        insights.append("Consider learning Data Analysis for better job opportunities.")

    if len(skills) < 4:
        insights.append("Adding more technical skills can strengthen your resume.")

    insights.append("Adding real-world projects can significantly improve your resume strength.")

    return insights
