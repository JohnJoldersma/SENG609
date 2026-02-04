import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt


def encodeData():
    df = pd.read_csv("tennis_data.csv")
    print(f"Data : \n{df}")
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    encoder = OneHotEncoder(sparse_output=False)

    one_hot_encoded = encoder.fit_transform(df[categorical_columns])

    one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

    df_encoded = pd.concat([df, one_hot_df], axis=1)

    df_encoded = df_encoded.drop(categorical_columns, axis=1)

    pd.set_option('display.max_columns', None)

    print(f"Encoded data : \n{df_encoded}")

    encoded_df = df_encoded.apply(pd.to_numeric, errors='coerce')

    numeric_cols_list = encoded_df.select_dtypes(include=[np.number]).columns.tolist()
    # Create the X and y arrays
    X = encoded_df[numeric_cols_list]
    y = encoded_df["play_yes"]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, y)

    tree.plot_tree(clf)
    plt.show()


encodeData()
