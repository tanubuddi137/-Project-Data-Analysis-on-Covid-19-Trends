# write a program on weather forecasting using Machine learning models


# read the data
def read_data(filename):
    """
    Read the data
    """
    data = pd.read_csv(filename)
    return data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(data):
    """
    Plot the data
    """
    plt.plot(data)
    plt.show()

# read the data
data = pd.read_csv('data/data.csv')
print(data.head())

# plot the data
plot_data(data['value'])
print(data.describe())

# split the data into train and test
train = data.sample(frac=0.8, random_state=200)
test = data.drop(train.index)
print(train.describe())
print(test.describe())

# plot the data
plot_data(train['value'])
plot_data(test['value'])

# split the data into features and labels
train_x = train.drop('value', axis=1)
train_y = train['value']
test_x = test.drop('value', axis=1)
test_y = test['value']

# plot the data
plot_data(train_y)
plot_data(test_y)

# import the model
from sklearn.linear_model import LinearRegression


# create the model
model = LinearRegression()
def train_model(model, train_x, train_y):
    """
    Train the model
    """
    model.fit(train_x, train_y)
    return model

print(train_model(model, train_x, train_y))


# make predictions
def make_predictions(model, test_x):
    """
    Make predictions
    """
    predictions = model.predict(test_x)
    return predictions

print(make_predictions(model, test_x))

# plot the predictions
def plot_predictions(predictions, test_y):
    """
    Plot the predictions
    """
    plt.scatter(range(len(test_y)), test_y)
    plt.plot(range(len(test_y)), predictions)
    plt.show()

print(plot_predictions(make_predictions(model, test_x), test_y))
print(test_y)

# calculate the error
def calculate_error(predictions, test_y):
    """
    Calculate the error
    """
    error = np.mean(np.abs(predictions - test_y))
    return error


print(calculate_error(make_predictions(model, test_x), test_y))
