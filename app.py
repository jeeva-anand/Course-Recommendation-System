import streamlit as st
import pandas as pd

from src.utils import load_model
from src.recommender import CourseRecommender

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="CourseFlix 🎬",
    layout="wide"
)

# ----------------------------
# LOAD DATA
# ----------------------------
data = pd.read_csv("data/udemy_course_data.csv")

# vectorizer = load_model("models/vectorizer.pkl")
# matrix = load_model("models/similarity_matrix.pkl")


matrix = 0.0

model = CourseRecommender(matrix, data)

# ----------------------------
# HERO SECTION
# ----------------------------
st.title("🎬 CourseFlix")
st.subheader("Find your next skill like you find movies on Netflix")

course = st.selectbox(
    "Search a course",
    data["course_title"].values
)

top_n = 10

if st.button("🎯 Get Recommendations"):

    results = model.recommend(course, top_n)

    # ----------------------------
    # SECTION 1: RECOMMENDATIONS
    # ----------------------------
    st.markdown("## 🔥 Recommended for You")

    cols = st.columns(5)

    for i, row in results.head(5).iterrows():

        with cols[i % 5]:

            st.markdown("### 📘")
            st.write(row["course_title"])
            st.caption(f"💰 ${row['price']}")
            st.progress(float(row["similarity_score"]))

# ----------------------------
# SECTION 2: TRENDING
# ----------------------------
st.markdown("## 🚀 Trending Courses")

trending = data.sample(10)

cols = st.columns(5)

for i, row in trending.iterrows():

    with cols[i % 5]:

        st.markdown("### 🎥")
        st.write(row["course_title"])
        st.caption(f"💰 ${row['price']}")

# ----------------------------
# SECTION 3: BUDGET PICKS
# ----------------------------
st.markdown("## 💰 Budget-Friendly Courses")

budget = data[data["price"] < data["price"].median()].sample(10)

cols = st.columns(5)

for i, row in budget.iterrows():

    with cols[i % 5]:

        st.markdown("### 🟢")
        st.write(row["course_title"])
        st.caption(f"💰 ${row['price']}")
