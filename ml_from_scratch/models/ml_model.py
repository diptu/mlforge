# ml_model.py
from abc import ABC, abstractmethod

class MLModel(ABC):
    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass
