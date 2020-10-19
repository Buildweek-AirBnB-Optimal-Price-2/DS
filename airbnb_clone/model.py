import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


'''Predicts airbnb rental price based on parameters.'''


def predict_price(model, rental_parameters):
    """Predicts airbnb rental price based on parameters.

    Args:
        model (LinReg): LinearRegression model from train_model()
        rental_parameters (list): List of user-selected parameters

    Returns:
        float: Predicted price of rental property
    """

    model = model
    #                    [[lon,                  lat,                  min_nights]]
    return model.predict([[rental_parameters[0], rental_parameters[1], rental_parameters[2]]])


def train_model():
    """Instanciates and trains the model.
    """

    url = 'https://raw.githubusercontent.com/lukiepookieofficial/NYC-AirBNB/main/AB_NYC_2019.csv'
    df = pd.read_csv(url)

    features = ['longitude', 'latitude', 'minimum_nights']
    target = ['price']

    x_train = df[features]
    y_train = df[target]

    X_train, _X_test, y_train, _y_test = train_test_split(x_train, y_train, test_size=0.25,
                                                          random_state=1138)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model
