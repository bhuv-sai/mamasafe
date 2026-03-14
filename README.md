<h1 align="center">🤰 MamaSafe – AI Pregnancy Risk Checker 🚑</h1>

<p align="center">
  An AI-powered web application that analyzes symptoms during late-stage pregnancy (32–40 weeks) and provides risk-based guidance to help mothers identify potential complications early.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Backend-FastAPI-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/Deployment-Docker-blue?style=for-the-badge&logo=docker">
  <img src="https://img.shields.io/badge/Cloud-Render-purple?style=for-the-badge">
</p>

---

# 🔗 Live Demo

👉 https://mamasafe.onrender.com/app/

---

# 📖 Project Overview

Late-stage pregnancy (weeks **32–40**) can involve many symptoms that may be either normal or signs of serious complications.

In many rural and semi-urban areas, immediate medical consultation may not always be available. **MamaSafe** helps bridge this gap by providing a **symptom-based AI risk assessment system**.

The system evaluates combinations of symptoms and classifies the pregnancy condition into risk categories.

The goal is **not to diagnose**, but to provide **early risk awareness and guidance**.

---

# 🛠️ Tech Stack

- Python
- FastAPI
- Scikit-learn
- NumPy
- Pandas
- HTML / CSS / JavaScript
- Docker
- Uvicorn
- Pickle (Model Serialization)
- Git & GitHub

---

# ⚙️ Machine Learning Workflow

1️⃣ Data Simulation & Dataset Creation  
2️⃣ Data Preprocessing  
3️⃣ Feature Engineering  
4️⃣ Model Training using Decision Tree / Classification Model  
5️⃣ Model Serialization using Pickle  
6️⃣ API Integration using FastAPI  
7️⃣ Frontend Integration  
8️⃣ Docker Containerization  
9️⃣ Cloud Deployment using Render

---

# 📊 Model Risk Classification

The system categorizes symptoms into three risk levels:

| Risk Level | Meaning |
|-------------|---------|
| ✅ Normal | Symptoms are common during late pregnancy |
| ⚠️ Monitor | Symptoms should be monitored and doctor consultation recommended |
| 🚨 Emergency | Immediate medical attention required |

---

# 🖥️ Application Features

✔ AI-based pregnancy symptom analysis  
✔ Risk classification (Normal / Monitor / Emergency)  
✔ Explainable symptom reasoning  
✔ Clean and simple user interface  
✔ Fast API-based backend  
✔ Docker-based deployment  
✔ Cloud hosted application  


## 📂 Project Structure
---
mamasafe/
│
├── app/
│ ├── main.py
│
├── models/
│ └── pregnancy_model.pkl
│
├── frontend/
│ └── index.html
│
├── notebooks/
│ ├── train.ipynb
│ └── test.ipynb
│
├── Dockerfile
├── requirements.txt
├── setup.py
├── README.md


---

# 🚀 Run Locally

### 1️⃣ Clone the repository
---

## 🚀 Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/bhuv-sai/mamasafe.git
cd mamasafe
```
### 2️⃣ Install dependencies
``` bash
pip install -r requirements.txt
```
### 3️⃣ Run FastAPI Server
```bash
uvicorn app.main:app --reload
```

### 4️⃣ Open in Browser
```bash
http://127.0.0.1:8000
```

### 4️⃣ Open in Browser
```bash
http://127.0.0.1:8000
```

## 🐳 Docker Deployment
### Build Docker Image
```bash
docker build -t mamasafe .
```

### Run Docker Container
```bash
docker run -p 8000:8000 mamasafe
```

## 📌 Example Symptom Input

Gestational Week: 36
Pain Level: Moderate
Contractions: Frequent
Bleeding: No
Fetal Movement: Normal
Swelling: Severe
Vision Disturbance: No


## 🎯 Future Improvements

Mobile application support

Real-time pregnancy monitoring

Integration with hospital systems

Advanced deep learning model

Multi-language support for rural users

## 👩‍💻 Authors

Janaki Sravanthi Paluchuri
Bhuvana Sai Mamidi
Neeraja Seerapu

