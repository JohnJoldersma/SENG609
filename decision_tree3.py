import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def runTree(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # clf = tree.DecisionTreeClassifier()
    # clf = clf.fit(X_train, y_train)
    # y_pred = clf.predict(X_test)

    regr = DecisionTreeRegressor(max_depth=5)
    regr.fit(X, y)

    # Predict
    # X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
    y_predict = regr.predict(X_test)

    # Plot the results
    plot_tree(regr,
              filled=True,
              rounded=True,
              fontsize=10
              )
    plt.title("Decision Tree Regressor Visualization")
    plt.show()

    # plt.figure()
    # plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
    # plt.plot(X_test, y_predict, color="cornflowerblue", label="max_depth=5", linewidth=2)
    # plt.xlabel("data")
    # plt.ylabel("target")
    # plt.title("Decision Tree Regression")
    # plt.legend()
    # plt.show()

    # check error rate
    print("Mean squared error:")
    print(mean_squared_error(y_test, y_predict))
    print("R2 score:")
    print(r2_score(y_test, y_predict))

    # accuracy = accuracy_score(y_test, y_predict)
    # Error rate is 1 - accuracy
    # error_rate = 1 - accuracy
    # print(f"Accuracy: {accuracy}, Error Rate: {error_rate}")

    # tree.plot_tree(clf)
    # plt.show()
