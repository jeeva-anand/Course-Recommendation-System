from sklearn.feature_extraction.text import TfidfVectorizer


def build_vectorizer(text):

    tfidf = TfidfVectorizer(
        stop_words="english"
    )

    matrix = tfidf.fit_transform(text)

    return tfidf, matrix
