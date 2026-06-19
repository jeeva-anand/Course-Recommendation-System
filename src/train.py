from data_loader import load_data
from preprocess import clean_titles
from vectorizer import build_vectorizer
from utils import save_model

from sklearn.metrics.pairwise import cosine_similarity


df = load_data(
    "../data/raw/udemy_course_data.csv"
)



df = clean_titles(df)

 

vectorizer, matrix = build_vectorizer(
    df["clean_title"]
)



similarity_matrix = cosine_similarity(matrix)

save_model(
    vectorizer,
    "../models/vectorizer.pkl"
)

save_model(
    similarity_matrix,
    "../models/similarity_matrix.pkl"
)


