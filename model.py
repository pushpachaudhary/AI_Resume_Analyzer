import re

# Predefined skills database
skills_db = [
    "python", "java", "c", "c++", "html", "css", "javascript",
    "machine learning", "ai", "data science", "sql"
]

def extract_skills(text):
    found = []
    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return found

def calculate_score(skills):
    return len(skills) * 10

def get_suggestion(score):
    if score < 30:
        return "Add more technical skills and projects."
    elif score < 60:
        return "Good, but can improve with advanced skills."
    else:
        return "Excellent resume!"

def analyze_resume(text):
    skills = extract_skills(text)
    score = calculate_score(skills)
    suggestion = get_suggestion(score)

    return {
        "skills": skills,
        "score": score,
        "suggestion": suggestion
    }