import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from preceptron import Perceptron

# Load dataset
data = pd.read_csv("data/dataset.csv")

# Features and labels
X = data[['x1','x2']].values
y = data['label'].values

# Train model
model = Perceptron(lr=0.1, epochs=10)
model.fit(X, y)

# Predictions
predictions = model.predict(X)
print("Predictions:", predictions)

# Plot data
plt.scatter(X[:,0], X[:,1], c=y)

# Decision boundary
x0 = np.linspace(0,4,10)
x1 = -(model.weights[0] * x0 + model.bias) / model.weights[1]

plt.plot(x0, x1)

plt.title("Perceptron Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Save result
plt.savefig("output/output.png")

plt.show()