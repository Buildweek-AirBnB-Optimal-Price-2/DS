from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .model import predict_price
import json
import pandas as pd


def create_app():
    '''Create and configure an instance of our Flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Luke Melto\\Documents\\GitHub\\\DS\\airbnb_clone\\airbnb_clone.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB = SQLAlchemy()
    DB.init_app(app)  # Connect Flask app to SQLAlchemy DB

    @app.route('/')
    def root():
        return render_template('index.html', title='Home')

    @app.route('/predict', methods=['GET', 'POST'])
    def predict():
        """ features = [request.form.values()]
        json_dict = {}

        json_dict['latitude'] = features[0]
        json_dict['longitude'] = features[1]
        json_dict['min_rooms'] = features[2]

        req = jsonify(json_dict) """
        req = request.json.get("parameters")
        json_format = json.dumps(req)
        df = pd.read_json(json_format)

        prediction = predict_price(df)

        return (jsonify(prediction))

    return app
