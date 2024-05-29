# Run this program on your local python
# interpreter, provided you have installed
# the required libraries.

# Importing the required packages
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd

# balance_data = pd.read_csv("E:\PhatTrienCacHeThongTM\Treeeee.csv", encoding='latin1')
iowa_file_path = "E:\PhatTrienCacHeThongTM\data.csv"
home_data = pd.read_csv(iowa_file_path, encoding='latin1')
# print(home_data)
# home_data


def main(a,b,c,d,e):
    home_data['Danhgia'] = home_data['Danhgia'].replace('Tot', 3)
    home_data['Danhgia'] = home_data['Danhgia'].replace('Kha', 2)
    home_data['Danhgia'] = home_data['Danhgia'].replace('Trung Binh', 1)
    home_data['Danhgia'] = home_data['Danhgia'].replace('Kem', 0)

    home_data['NhanxetTT'] = home_data['NhanxetTT'].replace('Gioi', 3)
    home_data['NhanxetTT'] = home_data['NhanxetTT'].replace('Kha', 2)
    home_data['NhanxetTT'] = home_data['NhanxetTT'].replace('Trung Binh', 1)
    home_data['NhanxetTT'] = home_data['NhanxetTT'].replace('Kem', 0)

    home_data['TrinhDoNN'] = home_data['TrinhDoNN'].replace('Advanced', 5)
    home_data['TrinhDoNN'] = home_data['TrinhDoNN'].replace('Upper-Intermediate', 4)
    home_data['TrinhDoNN'] = home_data['TrinhDoNN'].replace('Intermediate', 3)
    home_data['TrinhDoNN'] = home_data['TrinhDoNN'].replace('Pre-Intermediate', 2)
    home_data['TrinhDoNN'] = home_data['TrinhDoNN'].replace('Elementary', 1)
    home_data['TrinhDoNN'] = home_data['TrinhDoNN'].replace('Beginner', 0)

    home_data['KiNangLVN'] = home_data['KiNangLVN'].replace('Gioi', 3)
    home_data['KiNangLVN'] = home_data['KiNangLVN'].replace('Kha', 2)
    home_data['KiNangLVN'] = home_data['KiNangLVN'].replace('Trung Binh', 1)
    home_data['KiNangLVN'] = home_data['KiNangLVN'].replace('Kem', 0)

    home_data['KiNangGT'] = home_data['KiNangGT'].replace('Gioi', 3)
    home_data['KiNangGT'] = home_data['KiNangGT'].replace('Kha', 2)
    home_data['KiNangGT'] = home_data['KiNangGT'].replace('Trung Binh', 1)
    home_data['KiNangGT'] = home_data['KiNangGT'].replace('Kem', 0)

    home_data['HocLuc'] = home_data['HocLuc'].replace('Gioi', 3)
    home_data['HocLuc'] = home_data['HocLuc'].replace('Kha', 2)
    home_data['HocLuc'] = home_data['HocLuc'].replace('Trung Binh', 1)
    home_data['HocLuc'] = home_data['HocLuc'].replace('Kem', 0)

    # features_list = ["NhanxetTT", "TrinhDoNN","KiNangLVN", "KiNangGT", "HocLuc"]
    #
    # for column in features_list:
    #     home_data[column] = pd.factorize(home_data[column])[0]

    home_data['Danhgia']
    y = home_data.Danhgia

    # home_data

    features_list = ["NhanxetTT", "TrinhDoNN", "KiNangLVN", "KiNangGT","HocLuc"]

    X = home_data[features_list].values

    train_X, val_X, train_y, val_y = train_test_split(X, y,test_size=0.3,random_state=42)

    hd_model = DecisionTreeRegressor()
    hd_model.fit(train_X, train_y)

    # val_X =[[3,6,3,3,3]]
    val_X =[[a,b,c,d,e]]
    predictions = hd_model.predict (val_X)
    # mea = mean_absolute_error(val_y, predictions)

    # print(predictions)
    return predictions





























# # Function importing Dataset
# def importdata():
#     balance_data = pd.read_csv(
#         'https://archive.ics.uci.edu/ml/machine-learning-' +
#         'databases/balance-scale/balance-scale.data',
#         sep=',', header=None)
#     balance_data = pd.read_csv("E:\PhatTrienCacHeThongTM\Treeeee.csv", encoding='latin1')
#
#     # Printing the dataswet shape
#     print("Dataset Length: ", len(balance_data))
#     print("Dataset Shape: ", balance_data.shape)
#
#     # Printing the dataset obseravtions
#     print("Dataset:")
#     print(balance_data.head())
#     return balance_data
#
#
# # Function to split the dataset
# def splitdataset(balance_data):
#     # Separating the target variable
#     X = balance_data.values[:, 1:5]
#     Y = balance_data.values[:, 0]
#
#     # Splitting the dataset into train and test
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, Y, test_size=0.3, random_state=100)
#
#     return X, Y, X_train, X_test, y_train, y_test
#
#
# # Function to perform training with giniIndex.
# def train_using_gini(X_train, X_test, y_train):
#     # Creating the classifier object
#     clf_gini = DecisionTreeClassifier(criterion="gini",
#                                       random_state=100, max_depth=3, min_samples_leaf=5)
#
#     # Performing training
#     clf_gini.fit(X_train, y_train)
#     return clf_gini
#
#
# # Function to perform training with entropy.
# def tarin_using_entropy(X_train, X_test, y_train):
#     # Decision tree with entropy
#     clf_entropy = DecisionTreeClassifier(
#         criterion="entropy", random_state=100,
#         max_depth=3, min_samples_leaf=5)
#
#     # Performing training
#     clf_entropy.fit(X_train, y_train)
#     return clf_entropy
#
#
# # Function to make predictions
# def prediction(X_test, clf_object):
#     # Predicton on test with giniIndex
#     y_pred = clf_object.predict(X_test)
#     print("Predicted values:")
#     print(y_pred)
#     return y_pred
#
#
# # Function to calculate accuracy
# def cal_accuracy(y_test, y_pred):
#     print("Confusion Matrix: ",
#           confusion_matrix(y_test, y_pred))
#
#     print("Accuracy : ",
#           accuracy_score(y_test, y_pred) * 100)
#
#     print("Report : ",
#           classification_report(y_test, y_pred))
#
#
# # Driver code
# def main():
#     # Building Phase
#     data = importdata()
#     X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
#     clf_gini = train_using_gini(X_train, X_test, y_train)
#     clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
#
#     # Operational Phase
#     print("Results Using Gini Index:")
#
#     # Prediction using gini
#     y_pred_gini = prediction(X_test, clf_gini)
#     cal_accuracy(y_test, y_pred_gini)
#
#     print("Results Using Entropy:")
#     # Prediction using entropy
#     y_pred_entropy = prediction(X_test, clf_entropy)
#     cal_accuracy(y_test, y_pred_entropy)


# Calling main function
if __name__ == "__main__":
    main()