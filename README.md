---
title: Student Performance Analysis
sdk: docker
emoji: 🎓
colorFrom: blue
colorTo: green
app_port: 7860
---

# Student Performance Analysis

A Flask application to predict student performance based on various factors.

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Access the application at `http://localhost:7860`

## Deployment on Hugging Face Spaces

This project is configured for deployment on Hugging Face Spaces using Docker.

1. Create a new Space on [Hugging Face](https://huggingface.co/new-space).
2. Select **Docker** as the SDK.
3. Push your code to the Space's repository.
