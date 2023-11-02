import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

def load_data():
    housing = fetch_california_housing()
    data = housing.data
    target = housing.target
    feature_names = housing.feature_names
    df = pd.DataFrame(data, columns=feature_names)
    df['MedHouseValue'] = target
    return df

def split_data(data):
    X = data.drop('MedHouseValue', axis=1)
    Y = data['MedHouseValue']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=5)
    return X_train, X_test, Y_train, Y_test
