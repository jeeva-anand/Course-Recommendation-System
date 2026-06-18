
#  Course Recommendation System

### *Content-Based Recommendation Engine using NLP & Cosine Similarity*

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![ML](https://img.shields.io/badge/Machine%20Learning-NLP%20Based-orange?style=for-the-badge)
![Vectorization](https://img.shields.io/badge/TF--IDF-Cosine%20Similarity-yellow?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20App-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)

 

##  Overview

With thousands of online courses available on platforms like Udemy, learners often struggle to find relevant courses aligned with their interests.

This project builds an ** recommendation system** that suggests similar courses based on **semantic similarity of course titles using NLP techniques**.

 

##  Objective

To design a **content-based recommendation engine** that:

* Understands course semantics using NLP
* Converts text into numerical vectors
* Measures similarity between courses
* Recommends the most relevant learning resources

 

##  Problem Type

> 🔹 Content-Based Recommendation System
> 🔹 NLP + Information Retrieval Problem

 

##  How It Works

```text id="rec_flow_2"
Course Title
   ↓
Text Preprocessing (Stopwords + Cleaning)
   ↓
TF-IDF / Count Vectorization
   ↓
Cosine Similarity Matrix
   ↓
Ranking Similar Courses
   ↓
Top-N Recommendations
```

 

##  Dataset

* Udemy Course Dataset
* Features:

  * Course Title
  * URL
  * Price
  * Category (implicit via text)

 

##  Key Features

###  NLP Pipeline

* Stopword removal using NeatText
* Special character cleaning
* Text normalization

###  ML Engine

* CountVectorizer / TF-IDF Vectorizer
* Cosine Similarity Matrix
* Top-N ranking system

###  Recommendation System

* Input: Course name
* Output: Similar courses
* Ranked by similarity score

###  Deployment

* Interactive Streamlit web app
* Real-time course recommendations
* Clean UI for user interaction

 

##  Project Architecture

```text id="arch_01"
Raw Data
   ↓
Text Cleaning (NeatText)
   ↓
Vectorization (TF-IDF / CountVectorizer)
   ↓
Similarity Computation (Cosine Similarity)
   ↓
Recommendation Engine
   ↓
Streamlit Web App
```

 

##  Project Structure

```text id="structure_01"
Course-Recommendation-System/
│
├── data/
│   └── raw
        └── udemy_course_data.csv
│
├── models/
│   ├── vectorizer.pkl
│   └── similarity_matrix.pkl
│
├── src/
│   ├── preprocess.py
│   ├── data_loader.py
│   ├── vectorizer.py
│   ├── recommender.py
│   ├── train.py
│   ├── utils.py
│
├── app.py│
├── requirements.txt
└── README.md
```

 

##  How to Run Locally

### 1️ Clone Repository

```bash id="run_01"
git clone https://github.com/jeeva-anand/Course-Recommendation-System

cd Course-Recommendation-System
```

 

### 2️ Install Dependencies

```bash id="run_02"
pip install -r requirements.txt
```

 

### 3️ Train Model 

```bash id="run_03"
python train.py
```

This will generate:

* `vectorizer.pkl`
* `similarity_matrix.pkl`

 

### 4️ Run Streamlit App

```bash id="run_04"
streamlit run app.py
```

 

##  Features of Web App

*  Select any course from dropdown
*  Get similar course recommendations
*  View similarity scores
*  Instant real-time results
*  Interactive visualization of relevance

 

##  Sample Output

**Input:**

> “Machine Learning A-Z”

**Output:**

* Deep Learning Specialization (0.89)
* Python for Data Science (0.84)
* AI Fundamentals (0.81)

 

##  Key Insights

* Course titles alone contain strong semantic signals
* TF-IDF performs better than simple CountVectorizer
* Cosine similarity is effective for text-based recommendation
* Cleaning text significantly improves relevance

 

##  Evaluation Strategy

Since this is an unsupervised recommendation system:

* Qualitative evaluation (human relevance judgment)
* Similarity score distribution
* Top-N recommendation consistency


##  Tech Stack

* Python 
* Pandas / NumPy
* Scikit-learn
* NLP (NeatText, TF-IDF)
* Cosine Similarity
* Streamlit


# If You Like This Project

Feel free to star ⭐ the repository and contribute improvements!
