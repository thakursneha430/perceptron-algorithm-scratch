# perceptron-algorithm-scratch
The Perceptron Algorithm From Scratch 🧠 is a beginner-friendly machine learning project that demonstrates how a simple neural network can learn to classify data without using high-level ML libraries like scikit-learn.
In this project:
🐍 Implemented the Perceptron algorithm using Python and NumPy
📊 Trained the model on a small binary classification dataset
🤖 Predicts class labels (0 or 1) for new data points
🎨 Includes visualization of the decision boundary using Matplotlib

  <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/a4d3f745-7fd1-4ba5-82f3-eb21cb8e02b3" />


## Overview

This project implements the Perceptron algorithm from scratch using Python without relying on high-level machine learning libraries.The goal of this project is to understand how a basic neural network learns to classify data.The Perceptron is one of the earliest machine learning algorithms and forms the foundation of modern neural networks.The perceptron was introduced by Frank Rosenblatt (1957).It is a simple supervised learning algorithm used for binary classification problems.The model learns by adjusting weights and bias to correctly separate two classes of data using a decision boundary.

<img width="800" height="397" alt="image" src="https://github.com/user-attachments/assets/17a71000-6e3e-43e4-b5b7-66f3830498cf" />

## Project Structure
```
perceptron-from-scratch/
│── data/
│   └── dataset.csv
│── src/
│   └── perceptron.py
│── train.py
│── README.md
```

## Output

After training the model:
- Predictions are printed in the terminal
- A visualization graph is generated showing:
  - Data points
  - Decision boundary learned by the perceptron
    
  (<img width="640" height="480" alt="output" src="https://github.com/user-attachments/assets/b4656082-22fe-46ce-b8fd-512f490c2e17" />)

## How the Algorithm Works
1. Initialize weights and bias
2. Compute the linear combination of inputs and weights
3. Apply the activation function
4. Predict the class label
5. Update weights if prediction is incorrect

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
  
## Learning Outcome
This project helps understand:
- Basics of neural networks


