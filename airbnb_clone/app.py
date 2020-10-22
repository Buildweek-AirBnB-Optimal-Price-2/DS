from flask import Flask, render_template, request, jsonify
from .model import predict_price, train_model
import flask
import json
import pandas as pd


def create_app():
    '''Create and configure an instance of our Flask application'''
    app = Flask(__name__)
    model = train_model()

    @app.route('/')
    def root():
        return render_template('index.html', title='Home')

    @app.route('/predict', methods=['GET', 'POST'])
    def predict():

        json_data = flask.request.json
        json_format = json.dumps(json_data)
        df = pd.read_json(json_format, 'index')
        print(df)

        predict_parameters = []
        predict_parameters.append(df.iloc[0, 0])
        predict_parameters.append(df.iloc[1, 0])
        predict_parameters.append(df.iloc[2, 0])
        predict_parameters.append(df.iloc[3, 0])
        predict_parameters.append(df.iloc[4, 0])

        prediction = predict_price(model, predict_parameters)
        # print(prediction)

        predict_dict = {}
        predict_dict['predicted_value'] = float(prediction[0][:])
        print(prediction)
        print(predict_dict)
        return jsonify(predict_dict)

    return app
