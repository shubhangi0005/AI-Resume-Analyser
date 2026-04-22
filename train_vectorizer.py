from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# sample training data
texts = [
    "python machine learning data analysis",
    "java developer backend spring",
    "react frontend javascript html css"
]

# create vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# train it
tfidf.fit(texts)

# save as .pkl file
joblib.dump(tfidf, "vectorizer.pkl")

print("✅ vectorizer.pkl created successfully!")