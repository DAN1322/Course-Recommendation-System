#  Course Recommender System

A Machine Learning-based web application that recommends similar online courses based on a user's selected course. The recommendation engine uses **Content-Based Filtering** with **TF-IDF Vectorization** and **Cosine Similarity** to identify courses with similar descriptions and learning topics.

---

##  Project Overview

With the increasing number of online courses available on various learning platforms, finding the right course has become challenging. This project simplifies course discovery by recommending courses that are similar in content to the course selected by the user.

The application provides an intuitive web interface built with Flask, allowing users to receive personalized recommendations instantly.

---

## Features

- Recommend similar courses using Machine Learning
- Content-Based Recommendation System
- Fast recommendation generation using precomputed similarity matrix
- User-friendly Flask web application
- Clean and responsive interface
- Efficient text preprocessing pipeline

---

## System Architecture

```
                  Course Dataset
                        │
                        ▼
         Data Cleaning & Preprocessing
                        │
                        ▼
            TF-IDF Feature Extraction
                        │
                        ▼
          Cosine Similarity Matrix
                        │
                        ▼
          Recommendation Engine
                        │
                        ▼
              Flask Web Application
                        │
                        ▼
             Recommended Courses
```

---

##  Workflow

1. Load the course dataset.
2. Perform data cleaning and preprocessing.
3. Convert course descriptions into numerical vectors using TF-IDF.
4. Compute cosine similarity between all courses.
5. User selects a course.
6. The system identifies the most similar courses.
7. Display the top recommendations through the Flask web application.

---

##  Machine Learning Approach

The project uses a **Content-Based Filtering** recommendation technique.

### Algorithm Used

- TF-IDF (Term Frequency-Inverse Document Frequency)
- Cosine Similarity

### Why Content-Based Filtering?

- Does not require user ratings.
- Works efficiently for text-based datasets.
- Generates recommendations based on course content.
- Suitable for educational platforms with descriptive course information.

---

##  Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

### Data Processing

- Pandas
- NumPy

### Backend

- Flask

### Frontend

- HTML
- CSS
- Bootstrap

### Development Tools

- Jupyter Notebook
- Visual Studio Code

### Version Control

- Git
- GitHub

---

##  Project Structure

```
Course-Recommender-System/
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
├── dataset/
│   └── courses.csv
│
├── model/
│   ├── tfidf_vectorizer.pkl
│   └── similarity.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── notebook.ipynb
```

---

##  Data Preprocessing

The dataset undergoes several preprocessing steps before generating recommendations.

- Remove duplicate records
- Handle missing values
- Convert text to lowercase
- Remove punctuation
- Remove extra spaces
- Combine relevant text features

---

##  Evaluation

The recommendation system was evaluated based on:

- Recommendation relevance
- Response time
- Recommendation consistency
- User experience

### Results

- Accurate recommendations based on course content.
- Fast response using a precomputed similarity matrix.
- Stable and consistent recommendations.
- Smooth user interaction through the Flask interface.

---

##  Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Course-Recommender-System.git
```

### Navigate to the Project Directory

```bash
cd Course-Recommender-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

##  Screenshots

> Add screenshots of your application here.

Example:

- Home Page
- Course Selection Page
- Recommendation Results

---

##  Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- Deep Learning-based Recommendations
- User Authentication
- User Profile Management
- Course Rating and Reviews
- Personalized Learning Paths
- Deployment on Render, Railway, or Azure
- REST API Integration
- Real-time Course Search

---

##  Learning Outcomes

This project helped in gaining practical experience with:

- Machine Learning
- Recommendation Systems
- Natural Language Processing (NLP)
- Feature Engineering
- Data Preprocessing
- Flask Web Development
- Model Integration
- Git & GitHub

---

##  Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Create a Pull Request.

---

##  License

This project is licensed under the MIT License.

---

##  Author

**Dnyanesh Patil**

- GitHub: https://github.com/DAN1322
- LinkedIn: Dnyanesh Patil
- Email: patildnyaneshp737@gmail.com

---

##  Support

If you found this project useful, consider giving it a star on GitHub. It helps others discover the project and motivates further improvements.
