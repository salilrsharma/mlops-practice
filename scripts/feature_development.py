import pandas as pd
import numpy as np

# Load data
try:
    data = pd.read_csv(r"./data/AAPL.csv")
    print("financial data loaded")
except Exception as ex:
    print(ex)

print(data.head(5))

feature_closing_price = data['Adj Close'].values

try:
    np.savetxt(fname="./data/feature_closing_price.out", X=feature_closing_price, delimiter=',')
    print("Features saved")
except Exception as ex:
    print(ex)