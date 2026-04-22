import json

def match_skills(resume_text, jd_text):
    with open("data/skills_db.json") as f:
        skills = json.load(f)

    resume_skills = [s for s in skills if s in resume_text]
    jd_skills = [s for s in skills if s in jd_text]

    missing = list(set(jd_skills) - set(resume_skills))

    return resume_skills, missing