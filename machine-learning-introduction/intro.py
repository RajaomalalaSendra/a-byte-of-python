import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle


#loading our data as a panda
df = pd.read_csv('~/Downloads/winequality-red.csv', delimiter=";")

#getting only the column called quality
label = df['quality']

#getting every column except for quality
features = df.drop('quality', axis=1)

#defining our linear regression estimator and training it with our wine data
regr = linear_model.LinearRegression()
regr.fit(features, label)

#serializing our model to a file called model.pkl
pickle.dump(regr, open("model.pkl","wb"))

#loading a model from a file called model.pkl
model = pickle.load(open("model.pkl","rb"))