# insights_engine.py

def generate_insights(skills):

    insights = []

    skills = [s.lower() for s in skills]

    # Programming
    if "programming" not in skills:
        insights.append("Strengthen programming skills such as Python, Java or C++.")

    # Web Development
    if "web development" not in skills:
        insights.append("Adding HTML, CSS and JavaScript will improve opportunities in Web Development.")

    # Backend Development
    if "backend development" not in skills:
        insights.append("Learning backend technologies like Node.js, Django or Flask will expand development skills.")

    # Database
    if "database" not in skills:
        insights.append("Database knowledge such as SQL, MySQL or MongoDB is important for many tech roles.")

    # Data Skills
    if "data skills" not in skills:
        insights.append("Data analysis skills like Pandas, NumPy and visualization will strengthen your resume.")

    # AI / Machine Learning
    if "ai / machine learning" not in skills:
        insights.append("Learning Machine Learning or Artificial Intelligence can significantly boost career options.")

    # Cloud
    if "cloud computing" not in skills:
        insights.append("Cloud platforms such as AWS, Azure or Google Cloud are highly valued in industry.")

    # DevOps
    if "devops" not in skills:
        insights.append("Understanding DevOps tools like Docker, CI/CD or Git can improve your engineering profile.")

    # Mobile Development
    if "mobile development" not in skills:
        insights.append("Mobile app development using Flutter, Android or React Native can open new career paths.")

    # Skill count suggestion
    if len(skills) < 5:
        insights.append("Your resume currently shows limited skill diversity. Adding more technologies will improve your profile.")

    # Project suggestion
    insights.append("Building real-world projects and adding them to your resume will greatly strengthen your credibility.")

    # Portfolio suggestion
    insights.append("Maintaining a GitHub portfolio showcasing your work can improve recruiter visibility.")

    # default message
    if len(insights) == 0:
        insights.append("Your resume shows a strong and balanced skill set. Continue improving through projects and certifications.")

    return insights
