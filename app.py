from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# Allow cross-origin requests from any frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model artifacts
try:
    vectorizer = joblib.load('vectorizer.pkl')
    model = joblib.load('model.pkl')
except Exception as e:
    vectorizer = None
    model = None

class NewsRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "VeritasAI Backend API is active"}

@app.post("/predict")
def predict(request: NewsRequest):
    if not vectorizer or not model:
        return {"error": "Model files not found on server"}
        
    vec_text = vectorizer.transform([request.text])
    prediction = model.predict(vec_text)[0]
    probabilities = model.predict_proba(vec_text)[0]
    
    real_prob = float(probabilities[1]) * 100
    fake_prob = float(probabilities[0]) * 100
    
    return {
        "label": "REAL" if prediction == 1 else "FAKE",
        "real_probability": round(real_prob, 2),
        "fake_probability": round(fake_prob, 2)
    }
