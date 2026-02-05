import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd


def normalizeData():
    df = pd.read_csv("1101_data.csv")

    pd.set_option('display.max_columns', None)

    print(f"Data : \n{df}")

    columns_to_scale = ['ODO', 'CHRONO1', 'MILES']
    # scaler = MinMaxScaler()
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[columns_to_scale])

    df_scaled_subset = pd.DataFrame(scaled_features, columns=columns_to_scale, index=df.index)

    df[columns_to_scale] = df_scaled_subset

    # print("Normalized Data (Min-Max Scaling):")
    print("Standardized Data:")
    # print(scaled_features)
    print(df)

    return df, scaler

