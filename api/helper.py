import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def forecast(data):
  x = np.arange(1, len(data) + 1).reshape(-1, 1)  # Independent variable
  y = np.array(data)  # Dependent variable

  # Create and fit the linear regression model
  model = LinearRegression()
  model.fit(x, y)

  X = model.predict(x)

  # Make predictions for future observations
  future_X = np.array([[len(data) + 1], [len(data) + 2]])  # Future data points
  predicted_y = model.predict(future_X)

  slope = model.coef_[0]
  intercept = model.intercept_

  rmse = np.sqrt(mean_squared_error(y, X))

  return{
     'x' :x.tolist(),
     'y' : y.tolist(),
     'X' : X.tolist(),
     'future_x' : future_X.tolist(),
     'predicted_y' : predicted_y.tolist(),
     'slope':slope,
     'intercept':intercept,
     'rmse':rmse
  }

def corelation(data_type,year_from,year_to,data1,data2):
  base =2010
  f = (year_from-base)*12
  t = f+data_type+(year_to-year_from)*data_type

  x = data1[f:t]#independent
  y = data2 [f:t]#dependent

  # Create and fit the linear regression model
  model = LinearRegression()
  model.fit(x.reshape(-1, 1), y)

  X = model.predict(x.reshape(-1, 1))


  # Get the slope and intercept of the regression line
  slope = model.coef_[0]
  intercept = model.intercept_

  rmse = np.sqrt(mean_squared_error(y, X))

  return{
     'x' :x.tolist(),
     'y' : y.tolist(),
     'X' : X.tolist(),
     'slope':slope,
     'intercept':intercept,
     'rmse':rmse
  }

def corel(features,target):
   x = np.column_stack(features)
   y = target

   # Create a linear regression model
   model = LinearRegression()

   # Fit the model to the data
   model.fit(x,y)
   
   # Predict the target variable
   X= model.predict(x)


   # Retrieve the coefficients and intercept
   coefs = model.coef_
   intercept = model.intercept_

   

   rmse = np.sqrt(mean_squared_error(y, X))

   return{
      'x' :x.tolist(),
      'y' : y.tolist(),
      'X' : X.tolist(),
      'slope':coefs.tolist(),
      'intercept':intercept,
      'rmse':rmse
   }

