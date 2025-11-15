# Insurance Charge Predictor - Flutter App

A Flutter mobile application that connects to the Insurance Charge Prediction API to predict insurance charges based on user input.

## Features

- **Home Page**: Input form with all required fields
  - Age (number input)
  - Sex (dropdown: Male/Female)
  - BMI (decimal input)
  - Number of Children (number input)
  - Smoker (dropdown: Yes/No)
  - Region (dropdown: Northeast/Northwest/Southeast/Southwest)
  
- **Result Page**: Displays prediction results
  - Shows predicted insurance charge in formatted currency
  - Displays input summary
  - Error handling with clear error messages
  - Navigation back to form or home

## API Endpoint

The app connects to: `https://insurance-charge-predictor.onrender.com/predict`

## Getting Started

1. Install Flutter dependencies:
```bash
flutter pub get
```

2. Run the app:
```bash
flutter run
```

## Project Structure

```
lib/
├── main.dart                 # App entry point
├── models/
│   └── insurance_data.dart  # Data models
├── services/
│   └── api_service.dart     # API service for HTTP requests
└── pages/
    ├── home_page.dart       # Input form page
    └── result_page.dart     # Results display page
```

## Dependencies

- `http`: For making API requests
- `intl`: For currency formatting

## Requirements Met

✅ More than 1 page (Home page + Result page)
✅ Text fields for all input variables (6 fields total)
✅ Predict button
✅ Display area for predicted value
✅ Error message display for validation/API errors
✅ Well-organized, presentable UI
✅ Proper form validation
✅ Loading states
✅ Navigation between pages
