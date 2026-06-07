
# Student Performance Analysis

A comprehensive End-to-End Machine Learning project to predict student performance (Math Scores) based on various demographic and academic factors.

## Project Overview

The objective of this project is to understand how the student's performance (specifically in Math) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.

### Live Demo
[Student Performance Predictor on Hugging Face](https://aarya2603-studentperformancepredictor.hf.space/predictdata)

## Dataset Information

The dataset consists of the following features:

- **gender**: Sex of the student (Male/Female)
- **race_ethnicity**: Ethnicity groups (Group A, B, C, D, E)
- **parental_level_of_education**: Parent's education level (Associate's degree, Bachelor's degree, High school, Master's degree, Some college, Some high school)
- **lunch**: Type of lunch (Standard, Free/Reduced)
- **test_preparation_course**: Status of test preparation course (Completed, None)
- **reading_score**: Marks obtained in Reading
- **writing_score**: Marks obtained in Writing
- **math_score**: Marks obtained in Math (Target Variable)

## 🛠️ Project Structure

```text
├── artifacts/              # Data splits, model, and preprocessor pickles
├── notebook/               # Jupyter notebooks for EDA and Model Training
├── src/                    # Source code
│   ├── components/         # Modular components for ML lifecycle
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/           # Training and Prediction pipelines
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py        # Custom exception handling
│   ├── logger.py           # Logging configuration
│   └── utils.py            # Utility functions
├── templates/              # HTML templates for Flask UI
├── app.py                  # Flask Web Application entry point
├── Dockerfile              # Docker configuration
└── requirements.txt        # Project dependencies
```

## Tech Stack

- **Language**: Python 3.8+
- **Web Framework**: Flask
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, CatBoost, XGBoost
- **Containerization**: Docker
- **Deployment**: Hugging Face Spaces

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the application:**
   Open `http://localhost:7860` in your browser.

## Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t student-performance-app .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 7860:7860 student-performance-app
   ```
