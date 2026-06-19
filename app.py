from src.data_loader import load_data
import streamlit as st
import pandas as pd
from utils import load_model


from recommender import CourseRecommender


st.set_page_config(
    page_title="CourseFlix ",
    layout="wide"
)

data = pd.read_csv("./data/raw/udemy_course_data.csv")

vectorizer = load_model("./models/vectorizer.pkl")
matrix = load_model("./models/similarity_matrix.pkl")


model = CourseRecommender(matrix,data)


st.title(" CourseFlix")
st.subheader("Find your next skill like you find movies on Netflix")

course = st.selectbox(
    "Search a course",
    data["course_title"].values
)

top_n = 10

if st.button(" Get Recommendations"):

    results = model.recommend(course, top_n)

  
    st.markdown("##  Recommended for You")

    cols = st.columns(5)

    for i, row in results.head(5).iterrows():

        with cols[i % 5]:

            st.markdown("### 📘")
            st.write(row["course_title"])
            st.caption(f" ${row['price']}")
            st.progress(float(row["similarity_score"]))


st.markdown("## Trending Courses")

trending = data.sample(10)

cols = st.columns(5)

for i, row in trending.iterrows():

    with cols[i % 5]:

        st.markdown("### 📘")
        st.write(row["course_title"])
        st.caption(f" ${row['price']}")


st.markdown("## Budget-Friendly Courses")

budget = data[data["price"] < data["price"].median()].sample(10)

cols = st.columns(5)

for i, row in budget.iterrows():

    with cols[i % 5]:

        st.markdown("### 📘")
        st.write(row["course_title"])
        st.caption(f" ${row['price']}")
