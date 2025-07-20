# Student Exam Score Predictor

A machine learning web app built with **Streamlit** that predicts students' exam scores based on their personal and academic features. It uses a trained **Linear Regression** model to generate predictions in real time.

---

## Live Demo

👉 [Try the app on Streamlit]([https://student-exam-score-predictor-<your-app-id>.streamlit.app](https://student-exam-score-predictor-zhhaddx9mhmemmpqehxne9.streamlit.app/))

---

## Features

- Predicts exam scores based on user input
- Uses a trained regression model (`LinearRegression`)
- Interactive and clean UI built with Streamlit
- Fast and responsive — deployable instantly

---

## Tech Stack

- Python 3.x
- Streamlit
- scikit-learn
- joblib
- numpy

---

## How It Works

1. User enters personal and academic information
2. App converts categorical inputs to numerical
3. Model (`model.pkl`) predicts the score
4. Prediction is displayed instantly in the browser

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/<your-username>/student-exam-score-predictor.git
cd student-exam-score-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


