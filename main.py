import pandas as pd
import numpy as np
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from sklearn.preprocessing import StandardScaler

# --- Pydantic Model Definition ---
class InsuranceData(BaseModel):
    age: int = Field(..., gt=0) # Age must be greater than 0
    sex: Literal['male', 'female']
    bmi: float = Field(..., gt=0) # BMI must be greater than 0
    children: int = Field(..., ge=0) # Children must be greater than or equal to 0
    smoker: Literal['yes', 'no']
    region: Literal['northeast', 'northwest', 'southeast', 'southwest']

# --- FastAPI App Initialization and CORS Middleware ---
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# --- Load Model and Preprocessing Components ---
# Load the saved best model
# Ensure 'best_model.joblib' is in the same directory as this script
loaded_model = joblib.load('best_model.joblib')

# Re-instantiate and fit the StandardScaler
# This part needs to mimic the original preprocessing exactly.
# Ensure 'insurance.csv' is in the same directory as this script
DATA_PATH = 'insurance.csv'

# Load the original data to re-fit the scaler
original_df = pd.read_csv(DATA_PATH)

# Identify categorical columns (same as used in training)
categorical_cols = ['sex', 'smoker', 'region']

# Apply one-hot encoding to the original dataframe
original_df_encoded = pd.get_dummies(original_df, columns=categorical_cols, drop_first=False)

# Identify numerical features for scaling
numerical_features_to_scale = ['age', 'bmi', 'children']

# Initialize and fit the StandardScaler
scaler = StandardScaler()
scaler.fit(original_df_encoded[numerical_features_to_scale])

# Get the exact column order from the training features (X) for reindexing new data
X_columns_for_reindex = original_df_encoded.drop('charges', axis=1).columns


# --- Health Check Endpoint ---
@app.get("/")
async def root():
    """Root endpoint - returns API information."""
    return {
        "message": "Insurance Charge Prediction API",
        "status": "running",
        "docs": "/docs",
        "endpoints": {
            "predict": "/predict",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for deployment platforms."""
    try:
        # Verify model is loaded
        if loaded_model is None:
            return {"status": "unhealthy", "error": "Model not loaded"}
        
        # Verify scaler is fitted
        if scaler is None:
            return {"status": "unhealthy", "error": "Scaler not fitted"}
        
        return {
            "status": "healthy",
            "model_loaded": True,
            "scaler_fitted": True
        }
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

# --- Prediction Endpoint ---
@app.post("/predict")
async def predict_insurance_charge(data: InsuranceData):
    # Convert Pydantic model to pandas DataFrame
    new_data_df = pd.DataFrame([data.model_dump()])

    # Apply one-hot encoding to new data
    new_data_encoded = pd.get_dummies(new_data_df, columns=categorical_cols, drop_first=False)

    # Align columns with the training data (X_columns_for_reindex)
    # Fill missing columns (if a category wasn't present in new_data) with False
    new_data_aligned = new_data_encoded.reindex(columns=X_columns_for_reindex, fill_value=False)

    # Convert boolean columns to float64 for consistent numerical operations
    for col in new_data_aligned.columns:
        if new_data_aligned[col].dtype == 'bool':
            new_data_aligned[col] = new_data_aligned[col].astype(np.float64)

    # Apply the fitted scaler to numerical features of new_data
    new_data_aligned[numerical_features_to_scale] = scaler.transform(new_data_aligned[numerical_features_to_scale])

    # Make a prediction using the loaded model
    predicted_charge = loaded_model.predict(new_data_aligned)

    return {"predicted_insurance_charge": float(f"{predicted_charge[0]:.2f}")}

