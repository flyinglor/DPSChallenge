from email.mime import application
from flask import Flask, render_template, request, redirect, url_for, flash
from utils import *
import pandas as pd
import pickle
import json

application = Flask(__name__)
application.config['TEMPLATES_AUTO_RELOAD'] = True
model_path = './Model/linear_reg.pkl'

@application.route('/')
def hello():
    return 'Hello'

@application.route('/predict', methods=['GET', 'POST'])
def predict():
    content = request.json

    content = str(content).lower()
    json_acceptable_string = content.replace("'", "\"")
    content = json.loads(json_acceptable_string)

    if 'monatszahl' in content.keys():
        MONATSZAHL = trans_MONATSZAHL(content['monatszahl'])
    elif 'category' in content.keys():
        MONATSZAHL = trans_MONATSZAHL(content['category'])
    else:
        return "Missing Monatszahl(Category) value"

    
    if 'auspraegung' in content.keys():
        AUSPRAEGUNG = trans_AUSPRAEGUNG(content['auspraegung'])
    elif 'type' in content.keys():
        AUSPRAEGUNG = trans_AUSPRAEGUNG(content['type'])
    else:
        return "Missing Auspraegung(Type) value"


    if 'jahr' in content.keys():
        JAHR = trans_JAHR(content['jahr'])
    elif 'year' in content.keys():
        JAHR = trans_JAHR(content['year'])
    else:
        return "Missing Jahr(Year) value"

    if 'monat' in content.keys():
        MONAT = trans_MONAT(content['monat'])
    elif 'month' in content.keys():
        MONAT = trans_MONAT(content['month'])
    else:
        return "Missing Monat(Month) value"   

    df = pd.DataFrame([{'MONATSZAHL':MONATSZAHL,'AUSPRAEGUNG':AUSPRAEGUNG,'JAHR':JAHR,'MONAT':MONAT}])

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    prediction = model.predict(df)

    response = {
        "prediction": prediction[0]
    }

    return response


if __name__ == '__main__':
    app.run(debug=True)