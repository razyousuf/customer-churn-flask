# coding: utf-8
from flask import Flask, request, render_template #, jsonify
import pandas as pd
import pickle
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import OneHotEncoder
import logging

app = Flask(__name__)

# Configure the logging system to output to console
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load the pre-trained model, scaler, and one-hot encoder
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
#ohe = pickle.load(open('ohe.pkl', 'rb'))  # Loaded pre-fitted OneHotEncoder

# Feature names as they were used during training
model_features = [
    'tenure', 'monthlycharges', 'totalcharges', 'dependents_yes',
    'internetservice_fiber_optic', 'internetservice_no',
    'onlinesecurity_no', 'onlinesecurity_no_internet_service',
    'onlinebackup_no', 'onlinebackup_no_internet_service',
    'deviceprotection_no', 'deviceprotection_no_internet_service',
    'techsupport_no', 'techsupport_no_internet_service',
    'streamingtv_no_internet_service',
    'streamingmovies_no_internet_service', 'contract_1_year',
    'contract_2_year', 'contract_monthly', 'paperlessbilling_yes',
    'paymentmethod_electronic_check'
]

# Define the numeric feature columns (as used during training)
numeric_fields = ['tenure', 'monthlycharges', 'totalcharges']
#logger.debug(f"Features array: {numeric_fields}")

# Define the categorical feature columns (before OneHotEncoding)
categorical_fields = [
'dependents_yes', 'internetservice_fiber_optic', 'internetservice_no',
    'onlinesecurity_no', 'onlinesecurity_no_internet_service',
    'onlinebackup_no', 'onlinebackup_no_internet_service',
    'deviceprotection_no', 'deviceprotection_no_internet_service',
    'techsupport_no', 'techsupport_no_internet_service',
    'streamingtv_no_internet_service',
    'streamingmovies_no_internet_service', 'contract_1_year',
    'contract_2_year', 'contract_monthly', 'paperlessbilling_yes',
    'paymentmethod_electronic_check'
]


@app.route("/", methods=['GET'])
def load_page():
    # Render the main form page
    return render_template('home.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/', methods=['POST'])
def predict():
    try:
        # Extract numerical inputs
        tenure = float(request.form['tenure'])
        monthlycharges = float(request.form['MonthlyCharges'])
        totalcharges = float(request.form['TotalCharges'])
        
        # Extract categorical inputs and handle encoding
        dependents_yes = 1 if request.form['dependents'] == '1' else 0
        internet_service = request.form['internetservice']
        internetservice_fiber_optic = 1 if internet_service == 'fiber_optic' else 0
        internetservice_no = 1 if internet_service == 'no' else 0
        
        online_security = request.form['onlinesecurity']
        onlinesecurity_no = 1 if online_security == 'no' else 0
        onlinesecurity_no_internet_service = 1 if online_security == 'no_internet_service' else 0
        
        online_backup = request.form['onlinebackup']
        onlinebackup_no = 1 if online_backup == 'no' else 0
        onlinebackup_no_internet_service = 1 if online_backup == 'no_internet_service' else 0
        
        device_protection = request.form['deviceprotection']
        deviceprotection_no = 1 if device_protection == 'no' else 0
        deviceprotection_no_internet_service = 1 if device_protection == 'no_internet_service' else 0
        
        tech_support = request.form['techsupport']
        techsupport_no = 1 if tech_support == 'no' else 0
        techsupport_no_internet_service = 1 if tech_support == 'no_internet_service' else 0
        
        streaming_tv = request.form['streamingtv']
        streamingtv_no_internet_service = 1 if streaming_tv == 'no_internet_service' else 0
        
        streaming_movies = request.form['streamingmovies']
        streamingmovies_no_internet_service = 1 if streaming_movies == 'no_internet_service' else 0
        
        contract = request.form['contract']
        contract_1_year = 1 if contract == '1_year' else 0
        contract_2_year = 1 if contract == '2_year' else 0
        contract_monthly = 1 if contract == 'monthly' else 0
        
        paperlessbilling_yes = 1 if request.form['paperlessbilling'] == '1' else 0
        
        payment_method = request.form['paymentmethod']
        paymentmethod_electronic_check = 1 if payment_method == 'electronic_check' else 0
        
        # Assemble the feature array in the correct order
        features = [
            tenure, monthlycharges, totalcharges, dependents_yes,
            internetservice_fiber_optic, internetservice_no,
            onlinesecurity_no, onlinesecurity_no_internet_service,
            onlinebackup_no, onlinebackup_no_internet_service,
            deviceprotection_no, deviceprotection_no_internet_service,
            techsupport_no, techsupport_no_internet_service,
            streamingtv_no_internet_service, streamingmovies_no_internet_service,
            contract_1_year, contract_2_year, contract_monthly,
            paperlessbilling_yes, paymentmethod_electronic_check
        ]
        # Create DataFrame with model's feature names
        input_df = pd.DataFrame([features], columns=model_features)

       # Scale numeric fields
        input_df[numeric_fields] = scaler.transform(input_df[numeric_fields])
            #logger.debug(f"Scaled numeric fields:\n{input_df[numeric_fields].to_string(index=False)}")
        # Ensure compatibility with model's feature names
        input_df = input_df[model.feature_names_in_]
      
        # Log the reordered input DataFrame
        logger.debug(f"Reordered input DataFrame: {input_df.to_string(index=False)}")

        # Pass features to the model for prediction
        prediction = model.predict(input_df)[0]
        confidence = model.predict_proba(input_df)[0].max()

        if prediction == 1:
            output1 = "This customer is likely to churn!"
            output2 = f"Confidence: {confidence*100:.2f}%"
        else:
            output1 = "This customer is likely to continue!"
            output2 = f"Confidence: {confidence*100:.2f}%"

    except Exception as e:
        output1 = "Error processing the request"
        output2 = str(e)
        print(f"Error: {e}")

    # Pass output1 and output2 to the template
    return render_template("home.html", output1=output1, output2=output2)

if __name__ == "__main__":
    app.run(debug=True)
