import pandas as pd

from data_loader import load_data
from preprocess import clean_titles
from vectorizer import build_vectorizer
from utils import save_model

from sklearn.metrics.pairwise import cosine_similarity

# -----------------------
# Load Dataset
# -----------------------

df = load_data("../data/raw/udemy_course_data.csv")

# -----------------------
# NLP Cleaning
# -----------------------

df = clean_titles(df)

# -----------------------
# TF-IDF Vectorization
# -----------------------

vectorizer, matrix = build_vectorizer(
    df["clean_title"]
)

# -----------------------
# Similarity Matrix
# -----------------------

similarity_matrix = cosine_similarity(matrix)

# -----------------------
# Save Artifacts
# -----------------------

save_model(
    vectorizer,
    "../models/vectorizer.pkl"
)

save_model(
    similarity_matrix,
    "../models/similarity_matrix.pkl"
)

print("Training completed successfully!")
print("Saved:")
print("✓ vectorizer.pkl")
print("✓ similarity_matrix.pkl")
