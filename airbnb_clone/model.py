import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import category_encoders as ce
from tensorflow.keras.models import load_model
import pickle

# Loads transformation pipeline
infile = open("pipe.pkl", 'rb')
pipeline = pickle.load(infile)
infile.close()

# Loads model
model = load_model(
    r'C:\\Users\\Luke Melto\\Documents\\GitHub\\DS\\airbnb_clone\\new model\\saved_model\\my_model')


def predict_price(input, model=model, pipeline=pipeline):
    '''
    Function the runs input through the model and 
    returns the result
    '''

    x = pipeline.transform(input)
    suggested_price = model.predict(x)

    return suggested_price
