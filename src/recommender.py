import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class CourseRecommender:

    def __init__(self, matrix, df):
        self.matrix = matrix
        self.df = df
        self.similarity = cosine_similarity(matrix)

    def recommend(self, course_title, top_n=10):

        idx = self.df[
            self.df["course_title"] == course_title
        ].index[0]

        scores = list(enumerate(self.similarity[idx]))

        sorted_scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )[1:top_n+1]

        indices = [i[0] for i in sorted_scores]
        scores = [i[1] for i in sorted_scores]

        results = self.df.iloc[indices].copy()
        results["similarity_score"] = scores

        return results[
            ["course_title", "url", "price", "similarity_score"]
        ]
