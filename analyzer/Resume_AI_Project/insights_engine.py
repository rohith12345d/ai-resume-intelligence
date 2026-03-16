def generate_insights(skills,text):

    insights=[]

    if "github" not in text.lower():
        insights.append("Add a GitHub portfolio link.")

    if "project" not in text.lower():
        insights.append("Add project descriptions to showcase skills.")

    if len(skills)<4:
        insights.append("Include more technical skills.")

    insights.append("Use measurable achievements in resume.")

    return insights
