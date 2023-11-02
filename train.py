from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def train_model(X_train, Y_train):
    linear_model = LinearRegression()
    linear_model.fit(X_train, Y_train)
    return linear_model

def evaluate_model(model, X_train, X_test, Y_train, Y_test):
    Y_train_predict = model.predict(X_train)
    Y_test_predict = model.predict(X_test)
    rmse_train = np.sqrt(mean_squared_error(Y_train, Y_train_predict))
    rmse_test = np.sqrt(mean_squared_error(Y_test, Y_test_predict))
    return rmse_train, rmse_test
