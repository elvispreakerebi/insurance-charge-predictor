# Insurance Charge Prediction API

A FastAPI-based REST API for predicting insurance charges using a trained machine learning model.

## Python Version Compatibility

- **Recommended**: Python 3.11 or 3.12
- **Supported**: Python 3.13+ (may require newer package versions)
- **Minimum**: Python 3.8

If you encounter build errors with Python 3.13, consider using Python 3.11 or 3.12:
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Run the setup script (will clean up any existing venv)
./setup.sh

# Activate virtual environment
source venv/bin/activate

# Start the server
./run.sh
```

### Option 2: Manual Setup

#### 1. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Verify Setup

```bash
python test_setup.py
```

#### 4. Verify Files Are Present

Ensure the following files are in the project directory:
- `main.py` - FastAPI application
- `best_model.joblib` - Trained model file
- `insurance.csv` - Training dataset

#### 5. Run the API Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### GET /

Root endpoint that returns API information.

**Response:**
```json
{
  "message": "Insurance Charge Prediction API",
  "status": "running",
  "docs": "/docs",
  "endpoints": {
    "predict": "/predict",
    "health": "/health"
  }
}
```

### GET /health

Health check endpoint for monitoring and deployment platforms.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "scaler_fitted": true
}
```

### POST /predict

Predict insurance charges based on customer information.

**Request Body:**
```json
{
  "age": 25,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "northeast"
}
```

**Response:**
```json
{
  "predicted_insurance_charge": 12345.67
}
```

**Field Constraints:**
- `age`: Integer, must be greater than 0
- `sex`: Literal string - "male" or "female"
- `bmi`: Float, must be greater than 0
- `children`: Integer, must be greater than or equal to 0
- `smoker`: Literal string - "yes" or "no"
- `region`: Literal string - "northeast", "northwest", "southeast", or "southwest"

## Deployment to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Ensure `requirements.txt` is in the root directory
5. Deploy!

## Testing the API

### Using curl:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 25,
    "sex": "male",
    "bmi": 28.5,
    "children": 2,
    "smoker": "no",
    "region": "northeast"
  }'
```

### Using Python:
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "age": 25,
    "sex": "male",
    "bmi": 28.5,
    "children": 2,
    "smoker": "no",
    "region": "northeast"
}
response = requests.post(url, json=data)
print(response.json())
```

