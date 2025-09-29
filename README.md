# 🏦 Loan Approval Predictor

A FastAPI application that predicts loan approval status based on applicant information using a trained machine learning model. The pipeline includes preprocessing, so you can send raw input data directly.

---

## 📸 Project Preview

![Loan Approval Predictor](./assets/LoanApprovalPredictor/assets/1.png)
<!-- Place your project image at 'LoanApprovalPredictor/assets/project_preview.png' -->

---

## 🚀 Features

- **Predict loan approval status** using applicant details
- **Preprocessing pipeline** for categorical and numerical features
- **Machine learning model** for robust predictions
- **REST API** for easy integration

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone gh repo clone alihusnainawan/LoanApprovalPredictor
   cd LoanApprovalPredictor
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI app:**
   ```bash
   uvicorn app:app --reload
   ```

---

## 📋 Usage

- Access the interactive API docs at:  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- Example request body:
  ```json

{
  "no_of_dependents": 2,
  "education": 1,
  "self_employed": 0,
  "income_annum": 500000,
  "loan_amount": 200000,
  "loan_term": 12,
  "cibil_score": 750,
  "residential_assets_value": 300000,
  "commercial_assets_value": 0,
  "luxury_assets_value": 0,
  "bank_asset_value": 100000
}

  ```

---

## 📁 Project Structure

```
LoanApprovalPredictor/
│── app.py               # FastAPI app
│── model.pkl            # Trained pipeline
│── requirements.txt     # Dependencies
│── README.md            # Project description
│── assets/
│   └── project_preview.png   # Project image
```

---

## 👤 Author

**Ali Hasnain**  
_Data Science & ML Enthusiast_  
[LinkedIn](https://www.linkedin.com/in/ali-husnian01/)

---
