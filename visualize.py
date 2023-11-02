import matplotlib.pyplot as plt

def plot_predictions(Y_test, Y_test_predict):
    plt.figure(figsize=(10, 6))
    plt.scatter(Y_test, Y_test_predict)
    plt.plot([min(Y_test), max(Y_test)], [min(Y_test), max(Y_test)], color='red')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted Prices')
    plt.show()
