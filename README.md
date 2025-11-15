# Insurance Charge Prediction API

## Mission and Problem

This project addresses the challenge of predicting medical insurance charges for individuals based on their demographic and health characteristics. The problem involves building a machine learning model that can accurately estimate insurance costs using features such as age, BMI, smoking status, number of children, sex, and geographic region. The dataset used for training was obtained from Kaggle (insurance.csv), containing real-world insurance charge data. The solution provides both a REST API for programmatic access and a Flutter mobile application for end-user interaction, enabling accurate and accessible insurance charge predictions.

## Public API Endpoint

**Live API URL**: <a href="https://insurance-charge-predictor.onrender.com" target="_blank" rel="noopener noreferrer">https://insurance-charge-predictor.onrender.com</a>

**Swagger UI Documentation**: <a href="https://insurance-charge-predictor.onrender.com/docs" target="_blank" rel="noopener noreferrer">https://insurance-charge-predictor.onrender.com/docs</a>

The API is publicly accessible and can be tested directly using the Swagger UI interface. All endpoints are routable and do not require localhost access.

**Note**: Tests will be assessed using Swagger UI. The API endpoint is publicly available and returns predictions given input values.

## YouTube Demo Video

📹 **Demo Video** (5 minutes):

<div align="center">
  <a href="https://youtu.be/MMQ_lXdisIE">
    <img src="https://img.youtube.com/vi/MMQ_lXdisIE/maxresdefault.jpg" alt="Insurance Charge Predictor Demo Video" style="width:100%;max-width:640px;">
  </a>
</div>

<details>
<summary>Click to watch embedded video</summary>

<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/MMQ_lXdisIE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

</details>

The video demonstrates:
- API functionality and Swagger UI testing
- Flutter mobile app features
- End-to-end prediction workflow

## Dataset Source

The training dataset (`insurance.csv`) was obtained from **Kaggle** and contains insurance charge data with demographic and health-related features.

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

### 1. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Files Are Present

Ensure the following files are in the project directory:
- `main.py` - FastAPI application
- `best_model.joblib` - Trained model file
- `insurance.csv` - Training dataset

### 4. Run the API Server

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

## Running the Flutter Mobile App

### Prerequisites
- Flutter SDK installed (version 3.9.0 or higher)
- Android Studio / Xcode (for mobile development)
- An emulator/simulator or physical device

### Step-by-Step Instructions

1. **Navigate to the app directory:**
   ```bash
   cd app
   ```

2. **Install Flutter dependencies:**
   ```bash
   flutter pub get
   ```

3. **Run the app:**
   ```bash
   flutter run
   ```
   
   Or specify a device:
   ```bash
   flutter devices                    # List available devices
   flutter run -d <device-id>        # Run on specific device
   ```

4. **For Android:**
   - Ensure an Android emulator is running, or connect a physical device with USB debugging enabled
   - The app will automatically build and install

5. **For iOS (macOS only):**
   - Ensure Xcode is installed and an iOS simulator is available
   - Run `flutter run` to launch on the simulator

### App Features
- **Home Page**: Input form with 6 fields (age, sex, BMI, children, smoker, region)
- **Result Page**: Displays predicted insurance charge with input summary
- **Error Handling**: Validates inputs and displays clear error messages
- **API Integration**: Connects to the live API at <a href="https://insurance-charge-predictor.onrender.com" target="_blank" rel="noopener noreferrer">https://insurance-charge-predictor.onrender.com</a>

### Troubleshooting
- If dependencies fail to install, run `flutter clean` then `flutter pub get`
- Ensure your device/emulator has internet connectivity for API calls
- Check that the API endpoint is accessible: <a href="https://insurance-charge-predictor.onrender.com/health" target="_blank" rel="noopener noreferrer">https://insurance-charge-predictor.onrender.com/health</a>

## Testing the API

### Using Swagger UI (Recommended):
Visit <a href="https://insurance-charge-predictor.onrender.com/docs" target="_blank" rel="noopener noreferrer">https://insurance-charge-predictor.onrender.com/docs</a> and use the interactive interface to test the `/predict` endpoint.

### Using curl:
```bash
curl -X POST "https://insurance-charge-predictor.onrender.com/predict" \
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

url = "https://insurance-charge-predictor.onrender.com/predict"
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

