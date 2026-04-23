def calculate_score(similarity, missing_skills):
    score = similarity * 100 - len(missing_skills) * 2
    return max(0, min(100, int(score)))
