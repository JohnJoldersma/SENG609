import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib
import datetime as dt


def encodeData(df):
    # df = pd.read_csv("sample.csv")
    df['DATE'] = pd.to_datetime(df['DATE'], format='mixed')
    df['date_ordinal'] = df['DATE'].map(dt.datetime.toordinal)

    categorical_cols = ["TX"]

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

    # Create the X and y arrays
    X = encoded_df[["remainder__EQ", "remainder__ODO", "remainder__date_ordinal",
                    "remainder__CHRONO1", "remainder__CHRONO2",
                    "onehot__TX_00", "onehot__TX_0A"]]
    y = encoded_df["remainder__QTY"]

    return encoded_df


def runRegression(X, y, newInstance):

    # Split the data set in a training set (75%) and a test set (25%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # Create the Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Save the trained model to a file so we can use it to make predictions later
    joblib.dump(model, 'model.pkl')

    # Report how well the model is performing
    print("Model training results:")

    # Report an error rate on the training set
    mse_train = mean_absolute_error(y_train, model.predict(X_train))
    print(f" - Training Set Error: {mse_train}")

    # Report an error rate on the test set
    mse_test = mean_absolute_error(y_test, model.predict(X_test))
    print(f" - Test Set Error: {mse_test}")

    model = joblib.load('model.pkl')

    output_values = model.predict(newInstance)

    predicted_value = output_values[0]

    # print results
    print("Details:")
    print(f"- {newInstance[0]} ")
    print(f"Estimated value: {predicted_value:,.2f}")

    return predicted_value

