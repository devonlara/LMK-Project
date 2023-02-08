import numpy as np
from sklearn.model_selection import train_test_split

# Load the data
data = np.load('drone_data.npy')

# Split the data into features and labels
X = data[:, :-1]
y = data[:, -1].astype(int)


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
