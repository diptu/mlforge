# linear_regression.py
from math_utils import dot
from ml_model import MLModel

class LinearRegression(MLModel):
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0.0

    def fit(self, X, y):
        n_samples = len(X)
        n_features = len(X[0])

        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.epochs):
            y_pred = [dot(x, self.weights) + self.bias for x in X]

            dw = [0.0] * n_features
            db = 0.0

            for i in range(n_samples):
                error = y_pred[i] - y[i]
                for j in range(n_features):
                    dw[j] += error * X[i][j]
                db += error

            for j in range(n_features):
                self.weights[j] -= self.lr * (2 / n_samples) * dw[j]

            self.bias -= self.lr * (2 / n_samples) * db

    def predict(self, X):
        return [dot(x, self.weights) + self.bias for x in X]
