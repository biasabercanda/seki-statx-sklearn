import numpy as np
from sklearn.linear_model import LinearRegression

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

  return{
     'x' :x,
     'y' : y,
     'X' : X,
     'future_x' : future_X,
     'predicted_y' : predicted_y
  }