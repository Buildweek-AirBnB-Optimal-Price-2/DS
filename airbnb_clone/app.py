from flask import Flask, render_template, request, jsonify
from .model import predict_price
import flask
import json
import pandas as pd


def create_app():
    '''Create and configure an instance of our Flask application'''
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello World!'

    @app.route('/predict', methods=['GET', 'POST'])
    def predict():

        json_data = flask.request.json
        json_format = json.dumps(json_data)
        df = pd.read_json(json_format, 'index').T

        prediction = predict_price(df)

        predict_dict = {}
        predict_dict['predicted_value'] = float(prediction[0][:])
        return jsonify(predict_dict)

    return app
