# main.py
from linear_regression import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression(learning_rate=0.01, epochs=2000)
model.fit(X, y)

predictions = model.predict(X)
print(predictions)
