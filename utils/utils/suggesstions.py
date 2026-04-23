def generate_suggestions(missing_skills, score):
    suggestions = []

    if score < 50:
        suggestions.append("Improve your resume significantly by adding relevant projects and skills.")
    elif score < 75:
        suggestions.append("You are close! Try adding more relevant skills and improving formatting.")
    else:
        suggestions.append("Great job! Just fine-tune your resume for perfection.")

    for skill in missing_skills:
        suggestions.append(f"Consider adding {skill} to improve your chances.")

    return suggestions


def ai_chat_response(prompt, resume_skills, missing_skills, score):
    response = f"Based on your resume:\n\n"

    response += f"✔ Your score is {score}/100.\n"

    if score < 50:
        response += "You need strong improvements.\n"
    elif score < 75:
        response += "You're on the right track but can improve.\n"
    else:
        response += "Your resume looks strong!\n"

    if missing_skills:
        response += f"\nMissing skills: {', '.join(missing_skills)}\n"
        response += "Try adding these to improve your chances.\n"

    response += f"\nYour question: {prompt}\n"
    response += "Tip: Focus on aligning your resume with job requirements."

    return response


# ✅ FIXED VERSION (NO STRING PARSING BUGS)
def get_job_recommendations(matched_skills):
    import urllib.parse

    query = " ".join(matched_skills[:3]) if matched_skills else "fresher jobs"
    encoded = urllib.parse.quote(query)

    return [
        {
            "platform": "LinkedIn",
            "title": f"{query} Jobs",
            "link": f"https://www.linkedin.com/jobs/search/?keywords={encoded}"
        },
        {
            "platform": "Internshala",
            "title": f"{query} Jobs",
            "link": f"https://internshala.com/jobs/keywords-{encoded.replace('%20','-')}"
        },
        {
            "platform": "Indeed",
            "title": f"{query} Jobs",
            "link": f"https://www.indeed.com/jobs?q={encoded}"
        },
        {
            "platform": "Naukri",
            "title": f"{query} Jobs",
            "link": f"https://www.naukri.com/{encoded.replace('%20','-')}-jobs"
        },
        {
            "platform": "Glassdoor",
            "title": f"{query} Jobs",
            "link": f"https://www.glassdoor.co.in/Job/jobs.htm?sc.keyword={encoded}"
        }
    ]
