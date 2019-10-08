from math import sqrt
from project import timeit, data_completed, Prophet, plt, mean_squared_error, mean_absolute_error, \
    mean_absolute_percentage_error
tic=timeit.default_timer()

separation_date = '02-Aug-2018'
data_train_f1 = data_completed.loc[data_completed.index <= separation_date].copy()
data_test_f1 = data_completed.loc[data_completed.index > separation_date].copy()
_ = data_test_f1.rename(columns={'DAYTON_MW': 'TEST SET'})
_ = _.join(data_train_f1.rename(columns={'DAYTON_MW': 'TRAINING SET'}), how='outer')
_ = _.plot(figsize=(15,5), title='DAYTON consumption from 2004 to 2019', style='.')
model_f1 = Prophet(yearly_seasonality=True,weekly_seasonality=True,daily_seasonality=True)
model_f1.fit(data_train_f1.reset_index().rename(columns={'Datetime':'ds', 'DAYTON_MW':'y'}))
data_forecast = model_f1.predict(df=data_test_f1.reset_index().rename(columns={'Datetime':'ds'}))

f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
ax.scatter(data_test_f1.index, data_test_f1['DAYTON_MW'], color='r')
ax.set_title("Energy consumption forecasting in MW as of April 2nd")
#ax.set_xbound(upper='09-01-2004', lower='05-01-2019')
ax.set_ylim(0, 4000)
fig = model_f1.plot(data_forecast, ax=ax)

model_f1.plot_components(data_forecast)


print("Metrics for forecasting")
print ("\n")
print ("Root Mean Squared error is: ")
print( sqrt(mean_squared_error(y_true=data_test_f1['DAYTON_MW'],
                   y_pred=data_forecast['yhat'])))
print ("\n")

print ("Mean Absolute error is: ")
print(mean_absolute_error(y_true=data_test_f1['DAYTON_MW'],
                   y_pred=data_forecast['yhat']))
print ("\n")

print ("Mean Absolute percentage error is: ")
print(mean_absolute_percentage_error(y_true=data_test_f1['DAYTON_MW'],
                   y_pred=data_forecast['yhat']))
print("\n")

plt.show()
toc=timeit.default_timer()
print("\n Forecasting processing time: " + repr(toc - tic) + " sec") #elapsed time in seconds