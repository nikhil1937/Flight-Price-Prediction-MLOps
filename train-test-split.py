# Import train_test_split to divide the dataset
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create independent copies of training and testing features to avoid unintended modifications to the original data.
X_train = X_train.copy()
X_test = X_test.copy()