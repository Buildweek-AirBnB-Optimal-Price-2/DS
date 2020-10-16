from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .model import predict_price


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

    @app.route('/predict', methods=['POST'])
    def predict():

        features = [request.form.values()]
        prediction = predict_price(features)

        return render_template('index.html', prediction_text='Predicted price is ${}'.format(prediction))

    return app