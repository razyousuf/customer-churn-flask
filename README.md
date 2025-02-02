# customer-churn-flask

# Customer Churn Prediction - Flask Web App

## Overview
This is a Flask-based web application that predicts customer churn using a pre-trained machine learning model. The application takes user input, preprocesses the data, and provides a churn prediction result. This project is designed to assist businesses in identifying customers who are likely to churn, enabling proactive retention strategies.

## Features
- **Machine Learning Model Integration:** Uses a trained model (`model.pkl`) to predict customer churn.
- **Preprocessing Support:** Applies scaling transformations using `scaler.pkl`.
- **Web-based Interface:** Built using Flask and rendered with HTML templates.
- **Easy Deployment:** Install dependencies and run the app with minimal setup.

## Project Structure
```
📂 flask-churn-prediction
├── images/                   # Contains snapshots of the project
├── static/                   # Holds static files (CSS, JS, etc.)
├── templates/                # HTML templates for rendering Flask views
├── README.md                 # Project documentation (this file)
├── app.py                    # Main Flask application
├── model.pkl                 # Trained machine learning model
├── scaler.pkl                # Scaler for preprocessing input data
├── requirements.txt          # Required dependencies
```

## Installation & Setup
### **Prerequisites**
Ensure you have **Python 3.7+** installed. You may also want to use a virtual environment.

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/razyousuf/customer-churn-flask.git
cd customer-churn-flask
```

### **Step 2: Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Run the Flask App**
```bash
python app.py
```
The application will start on `http://127.0.0.1:5000/`.

## Usage
1. Open the web application in a browser (`http://127.0.0.1:5000/`).
2. Enter customer-related details in the input form.
3. Click the **Predict** button.
4. The model will process the input and display the churn prediction result.

## Machine Learning Model Details
- The model is trained using customer behavior data.
- It uses features such as contract type, monthly charges, tenure, etc.
- The model is stored in `model.pkl`, and the scaler for preprocessing is in `scaler.pkl`.

## Contributing
Contributions are welcome! If you’d like to improve this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to reach out to [https://github.com/razyousuf].
