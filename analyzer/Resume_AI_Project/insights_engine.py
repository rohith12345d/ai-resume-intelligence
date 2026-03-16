# insights_engine.py

def generate_insights(skills):

    insights = []

    if not skills:
        insights.append("No skills detected from the resume.")
        insights.append("Try uploading a clearer or more detailed resume.")
        return insights

    insights.append(f"{len(skills)} skills detected in your resume.")

    if "python" in skills:
        insights.append("Python skill detected — strong for data science and AI roles.")

    if "machine learning" in skills:
        insights.append("Machine Learning skill detected — good for AI engineer roles.")

    if "sql" not in skills:
        insights.append("Learning SQL can improve your chances for data roles.")

    if "data analysis" not in skills:
        insights.append("Consider learning Data Analysis for better career opportunities.")

    insights.append("Building real-world projects can significantly strengthen your resume.")

    return insights
