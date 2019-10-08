import csv
import pystan
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
plt.style.use('ggplot') # Make it pretty
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error, mean_absolute_error
# from os import path
# from typing import Union
from pandas import read_csv
# from pandas import datetime
# from math import sqrt
# from matplotlib import pyplot as plt
# import tensorflow as tf
import timeit
from IPython.display import Image

#time processing
tic=timeit.default_timer()

# # load dataset
# series = read_csv("csv/DAYTON_hourly.csv")
#
# # line plot
# series.plot()
# plt.show()
#
# print(series.head())
#

df = pd.read_parquet('csv/est_hourly.parquet', engine='pyarrow')
#viz of data split into different geographical region in the USA
Image(url="csv/PJMEvolution.jpg")

#data's checking
df.head()
# print(df.head())

#few stats on data such as counts, mean, min, max
df.describe().T
# print(df.describe().T)

#function to choose the file to work with

#loading data
data = pd.read_csv('csv/DAYTON_hourly.csv', index_col=[0], parse_dates=[0])
data_completed = pd.read_csv('csv/metered/DAYTON_hourly_completed.csv', index_col=[0], parse_dates=[0])
_ = data.plot(style='.', figsize=(15,5), color="Orange", title='DAYTON from 2004 to 2018')
_ = data_completed.plot(style='.', figsize=(15,5), color="Orange", title='DAYTON from 2018 to 2019')
print("Going through 1")

#creation of time features
def create_features(df, label=None):
    """
    Creates time series features from datetime index
    """
    df = df.copy()
    df['date'] = df.index
    df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.weekofyear

    X = df[['hour', 'dayofweek', 'quarter', 'month', 'year',
            'dayofyear', 'dayofmonth', 'weekofyear']]
    if label:
        y = df[label]
        return X, y
    return X


X, y = create_features(data, label='DAYTON_MW')

features_and_target = pd.concat([X, y], axis=1)
features_and_target.head()
print(features_and_target.head())

print("Going through 2")

# Splitting data between Validation and Test set following 80:20 practice.
# DAYTON begins in 2004, but most of data begin in 2002. We all set them at Jan. 2016
split_date = '01-Jan-2016'
data_train = data.loc[data.index <= split_date].copy()
data_test = data.loc[data.index > split_date].copy()



_ = data_test.rename(columns={'DAYTON_MW': 'TEST SET'})
_ = _.join(data_train.rename(columns={'DAYTON_MW': 'TRAINING SET'}), how='outer')
_ = _.plot(figsize=(15,5), title='DAYTON consumption', style='.')
#plt.show()
print("plot 2 done")

#data formatting
data_train.reset_index().rename(columns={'Datetime':'ds', 'DAYTON_MW':'y'}).head()

#Train model
model = Prophet(yearly_seasonality=True,weekly_seasonality=True,daily_seasonality=True)
model.fit(data_train.reset_index().rename(columns={'Datetime':'ds', 'DAYTON_MW':'y'}))

#Prediction on training set
data_test_forecast = model.predict(df=data_test.reset_index().rename(columns={'Datetime':'ds'}))


#Forecast vs actuals
f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
ax.scatter(data_test.index, data_test['DAYTON_MW'], color='r')
ax.set_title("Test set with forecasted vs metered")
fig = model.plot(data_test_forecast, ax=ax)

#metrics
print("Metrics for validation")
print ("\n")
print ("Mean Squared error is: ")
print( mean_squared_error(y_true=data_test['DAYTON_MW'],
                   y_pred=data_test_forecast['yhat']))
print ("\n")

print ("Mean Absolute error is: ")
print(mean_absolute_error(y_true=data_test['DAYTON_MW'],
                   y_pred=data_test_forecast['yhat']))
print ("\n")
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
print ("Mean Absolute percentage error is: ")
print(mean_absolute_percentage_error(y_true=data_test['DAYTON_MW'],
                   y_pred=data_test_forecast['yhat']))
print("\n")
plt.show
toc=timeit.default_timer()
print("\n 1st model Processing time: " + repr(toc - tic) + " sec") #elapsed time in seconds