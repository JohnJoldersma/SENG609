import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def encodeData():
    df = pd.read_csv("sample.csv")

    categorical_cols = ["EQ", "TX"]

    encoder = OneHotEncoder(sparse_output=False)

    preprocessor = ColumnTransformer(
        transformers=[
            ('onehot', encoder, categorical_cols)
        ],
        remainder='passthrough'
    )

    transformed = preprocessor.fit_transform(df)
    feature_names = preprocessor.get_feature_names_out()
    encoded_df = pd.DataFrame(transformed, columns=feature_names)

    pd.set_option('display.max_columns', None)

    print(f"Data : \n{df}")

    print(f"Encoded data : \n{encoded_df}")

    encoded_df = encoded_df.apply(pd.to_numeric, errors='coerce')

    numeric_cols_list = encoded_df.select_dtypes(include=[np.number]).columns.tolist()
    # Create the X and y arrays
    X = encoded_df[numeric_cols_list]
    y = encoded_df["remainder__QTY"]


def runTree(X, y):

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, y)

    tree.plot_tree(clf)


encodeData()
