import data_processing as dp
import train
import visualize

# Load and Split Data
california_data = dp.load_data()
X_train, X_test, Y_train, Y_test = dp.split_data(california_data)

# Train Model
model = train.train_model(X_train, Y_train)

# Evaluate Model
rmse_train, rmse_test = train.evaluate_model(model, X_train, X_test, Y_train, Y_test)
print("RMSE on Training Data: ", rmse_train)
print("RMSE on Testing Data: ", rmse_test)

# Visualize Predictions
Y_test_predict = model.predict(X_test)
visualize.plot_predictions(Y_test, Y_test_predict)
