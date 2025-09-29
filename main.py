from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("loan_approval_model.pkl")

# Define input schema
class LoanApplication(BaseModel):
    no_of_dependents: int
    education: int
    self_employed: int
    income_annum: float
    loan_amount: float
    loan_term: int
    cibil_score: float
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float

# Create FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Loan Approval Prediction API is running!"}

@app.post("/predict")
def predict_loan_status(data: LoanApplication):
    # Convert input to numpy array
    input_data = np.array([[ 
        data.no_of_dependents, data.education, data.self_employed, data.income_annum,
        data.loan_amount, data.loan_term, data.cibil_score, data.residential_assets_value,
        data.commercial_assets_value, data.luxury_assets_value, data.bank_asset_value
    ]])

    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Map to labels (change if your labels differ)
    result = "Approved" if prediction == 1 else "Rejected"
    
    return {"loan_status": result}
