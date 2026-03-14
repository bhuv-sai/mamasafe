# MamaSafe - AI Pregnancy Risk Checker

MamaSafe is an AI-based symptom checker designed to detect potential risks during the late stage of pregnancy (weeks 32–40).

## Features

- Symptom-based risk prediction
- Risk categories: Normal, Monitor, Emergency
- FastAPI backend
- Interactive frontend interface
- Machine learning model for prediction
- Docker support for deployment

## Project Architecture

Frontend (HTML / CSS / JS)
        ↓
FastAPI Backend
        ↓
ML Prediction Model
        ↓
Risk Classification
        ↓
User Guidance

## Installation

Clone the repository:

git clone https://github.com/yourusername/mamasafe.git

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --reload

## Docker Deployment

Build Docker image:

docker build -t mamasafe .

Run container:

docker run -p 8000:8000 mamasafe

## API Endpoint

POST /predict

Example Input:

{
  "week": 36,
  "pain": 2,
  "contractions": "Frequent",
  "bleeding": "No",
  "movement": "Normal",
  "swelling": "Mild",
  "vision": "Normal"
}

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Docker
- HTML/CSS/JavaScript

## Future Improvements

- Mobile application
- Real-time monitoring
- Integration with hospital systems