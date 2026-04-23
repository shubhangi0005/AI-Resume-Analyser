from sklearn.metrics.pairwise import cosine_similarity
import joblib

def get_similarity(text1, text2):
    vectorizer = joblib.load("models/vectorizer.pkl")
    vectors = vectorizer.transform([text1, text2])
    return cosine_similarity(vectors[0], vectors[1])[0][0]
