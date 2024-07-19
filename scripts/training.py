# import tensorflow as tf
import numpy as np

# Load data
data = np.loadtxt("./data/feature_closing_price.out", delimiter=',')

# Split data into train & test
n = len(data)
print(f"Length of original dataset: {n}")
train = data[0:int(n*0.7)]
print(f"Length of original dataset: {len(train)}")
val = data[int(n*0.7):int(n*0.9)]
print(f"Length of original dataset: {len(val)}")
test = data[int(n*0.9):]
print(f"Length of original dataset: {len(test)}")

# Normalize data using mean and standard deviation
train_mean = train.mean()
train_std = train.std()

train = (train - train_mean) / train_std
val = (val - train_mean) / train_std
test = (test - train_mean) / train_std




