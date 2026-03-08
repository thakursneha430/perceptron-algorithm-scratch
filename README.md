# perceptron-algorithm-scratch

![perceptron Graph](output/output.png)






Perceptron Algorithm From Scratch

Overview

This project implements the Perceptron algorithm from scratch using Python without relying on high-level machine learning libraries.
The goal of this project is to understand how a basic neural network learns to classify data.

The Perceptron is one of the earliest machine learning algorithms and forms the foundation of modern neural networks.

---

Algorithm Background

The perceptron was introduced by Frank Rosenblatt (1957).
It is a simple supervised learning algorithm used for binary classification problems.

The model learns by adjusting weights and bias to correctly separate two classes of data using a decision boundary.

---

Project Structure

perceptron-from-scratch
│
├── data
│   └── dataset.csv
│
├── src
│   ├── perceptron.py
│   └── train.py
│
├── results
│
└── README.md

---

Dataset

The dataset contains two input features and one label:

x1,x2,label
2,3,1
1,1,0
2,1,0
3,4,1
3,3,1
1,2,0
2,4,1
1,0,0

- x1, x2 → input features
- label → class (0 or 1)

---

How the Algorithm Works

1. Initialize weights and bias
2. Compute the linear combination of inputs and weights
3. Apply the activation function
4. Predict the class label
5. Update weights if prediction is incorrect
6. Repeat for multiple training epochs

---

Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

---

Output

After training the model:

- Predictions are printed in the terminal
- A visualization graph is generated showing:
  - Data points
  - Decision boundary learned by the perceptron

---

Learning Outcome

This project helps understand:

- Basics of neural networks
- How weights and bias update during training
- How a machine learning model learns to separate classes

---

Future Improvements

- Add larger datasets
- Implement multi-layer perceptron
- Compare with scikit-learn implementation
