# Insurance Premium Prediction API

A production-style **Machine Learning REST API** built with **FastAPI** for predicting insurance premium categories.

The project demonstrates how to take a trained machine learning model and deploy it as a containerized API with **automated testing, CI/CD, Docker Hub, and cloud deployment on Render**.

## 🚀 Live Demo

**Live API:**
https://insurance-premium-api-hq98.onrender.com

**Swagger API Documentation:**
https://insurance-premium-api-hq98.onrender.com/docs

The Swagger documentation allows you to interactively test the API endpoints, including the prediction endpoint.

---

## 🏗️ Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Install Dependencies
    ├── Run Pytest
    └── Build Docker Image
            │
            ▼
        Docker Hub
            │
            ▼
          Render
            │
            ▼
      Live FastAPI API
            │
            ▼
      Machine Learning Model
```

## ✨ Features

* FastAPI REST API
* Machine Learning model inference
* Pydantic request validation
* `/health` health-check endpoint
* `/predict` prediction endpoint
* Interactive Swagger documentation
* Automated testing with Pytest
* Docker containerization
* GitHub Actions CI pipeline
* Docker Hub image publishing
* Render cloud deployment
* Production-style project structure

## 📡 API Endpoints

### `GET /`

Returns a welcome message.

Example response:

```json
{
  "message": "Welcome to Insurance Premium!"
}
```

### `GET /health`

Checks whether the API and ML model are running correctly.

Example response:

```json
{
  "status": "ok",
  "version": "1.0.0",
  "model_loded": true
}
```

### `POST /predict`

Predicts the insurance premium category based on the provided customer information.

Example request:

```json
{
  "age": 35,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 8.0,
  "smoker": true,
  "city": "Istanbul",
  "occupation": "retired"
}
```

Example response:

```json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.43,
    "class_probs": {
      "High": 0.41,
      "Low": 0.16,
      "Medium": 0.43
    }
  }
}
```

## 🧪 Testing

The project uses **Pytest** for automated API testing.

Tests cover:

* Health endpoint
* Valid prediction request
* Invalid input validation

Tests are also executed automatically by GitHub Actions whenever changes are pushed to the `main` branch.

## 🐳 Docker

The application is containerized using Docker.

Docker image:

```text
numanawan/insurance-premium-api:latest
```

The Docker image is built automatically by GitHub Actions and pushed to Docker Hub.

## 🔄 CI/CD Pipeline

Every push to the `main` branch triggers the CI pipeline.

```text
Git Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Login to Docker Hub
   ↓
Push Docker Image
```

The Docker image can then be deployed to Render.

## ☁️ Deployment

The application is deployed using **Render**.

Deployment flow:

```text
GitHub
   ↓
GitHub Actions
   ↓
Docker Hub
   ↓
Render
   ↓
Live API
```

The deployed application is publicly accessible through the Live Demo links above.

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **Scikit-learn**
* **Pytest**
* **Docker**
* **GitHub Actions**
* **Docker Hub**
* **Render**

## 📁 Project Structure

```text
insurance-premium-api-cicd/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── config/
│
├── model/
│   └── model.pkl
│
├── schema/
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   └── test_perdict.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── app.py
└── requirements.txt
```

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/numanawan68/insurance-premium-api-cicd.git
cd insurance-premium-api-cicd
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app:app --reload --port 8012
```

Open Swagger:

```text
http://127.0.0.1:8012/docs
```

## 🎯 Project Goal

The main goal of this project is to demonstrate a complete machine learning deployment workflow — from a trained ML model to a **validated, tested, containerized, continuously integrated, and publicly deployed API**.
This project focuses not only on machine learning inference, but also on the engineering practices required to serve an ML model as a real-world API.
Note : i learned all tech stack from diff resources and i used ai tools to build this project thanks.
