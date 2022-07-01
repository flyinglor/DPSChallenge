from flask import Flask, render_template, request, redirect, url_for, flash
from utils import *
import pandas as pd
import pickle

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
model_path = './Model/linear_reg.pkl'

@app.route('/')
def hello():
    return 'Hello'

@app.route('/post', methods=['GET', 'POST'])
def predict():
    content = request.json

    MONATSZAHL = trans_MONATSZAHL(content['MONATSZAHL'])
    AUSPRAEGUNG = trans_AUSPRAEGUNG(content['AUSPRAEGUNG'])
    JAHR = trans_JAHR(content['JAHR'])
    MONAT = trans_MONAT(content['MONAT'])
    df = pd.DataFrame([{'MONATSZAHL':MONATSZAHL,'AUSPRAEGUNG':AUSPRAEGUNG,'JAHR':JAHR,'MONAT':MONAT}])

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    prediction = model.predict(df)

    return str(prediction[0])


if __name__ == '__main__':
    app.run(debug=True)