from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="FRONTEND", html=True), name="frontend")
# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Symptoms(BaseModel):
    email:str
    password:str
    week:int
    pain:int
    contractions:str
    bleeding:str
    movement:str
    swelling:str
    vision:str


@app.post("/predict")
def predict(data: Symptoms):

    print("Received from frontend:", data)

    risk = "Normal"
    message = (
"Risk Level: NORMAL\n\n"
"Detected Conditions\n"
"• Mild discomfort detected\n"
"• Irregular contractions observed\n"
"• Fetal movement is within normal range\n\n"
"Assessment\n"
"These symptoms are commonly experienced during the late stage of pregnancy "
"and currently do not indicate any serious complication.\n\n"
"Recommendation\n"
"• Continue regular prenatal care\n"
"• Stay hydrated and get adequate rest\n"
"• Monitor symptoms regularly"
)
    # 🚨 Emergency Conditions
    if data.bleeding == "Yes":
        risk = "Emergency"
        message = "Bleeding detected during late pregnancy. Visit hospital immediately."

    elif data.movement == "Reduced":
        risk = "Emergency"
        message = "Reduced fetal movement detected. Seek medical attention immediately."

    elif data.vision == "Blurred":
        risk = "Emergency"
        message = "Blurred vision may indicate preeclampsia. Visit hospital."

    elif data.pain == 3:
        risk = "Emergency"
        message = "Severe abdominal pain detected."

    # ⚠️ Monitor Conditions
    elif data.swelling == "Severe":
        risk = "Monitor"
        message = "Severe swelling detected. Monitor symptoms and consult a doctor."

    elif data.contractions == "Frequent":
        risk = "Monitor"
        message = "Frequent contractions detected. Monitor closely and contact doctor."

    elif data.pain == 2:
        risk = "Monitor"
        message = "Moderate pain detected. Monitor symptoms."

    # ✅ Normal
    else:
        risk = "Normal"
        message = "Symptoms look normal. Continue self-care and regular monitoring."

    return {
        "risk": risk,
        "message": message
    }
