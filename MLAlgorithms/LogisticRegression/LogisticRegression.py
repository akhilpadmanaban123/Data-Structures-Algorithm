# Logistic Regression : https://www.notion.so/akhilpadmanaban/Logistic-Regression-245e083f7553800a909bf04293c0c3c5
import numpy as np


def sigmoid(z):
    return 1 / 1 + np.exp(-z)

class LogisticRegression:
    def __init__(self, learning_rate = 0.01, num_iterations = 1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations 
        self.weights = None
        self.bias = None 
    
    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        for _ in range(self.num_iterations):
            predicted_linear_output = np.dot(X, self.weights.T) + self.bias 
            predicted_output = sigmoid(predicted_linear_output)
            # calculating the gradient - weights and bias
            dw = (1/num_samples)* np.dot(X.T, predicted_output - y)     # gradient w.r.t weights
            db = (1/num_samples)* np.sum(predicted_output - y)          # gradient w.r.t bias
            # updating the weights and bias

            self.weights = self.weights - self.learning_rate * dw 
            self.bias = self.bias - self.learning_rate * db 




    def predict(self, X):
        predicted_linear_output = np.dot(X, self.weights.T) + self.bias
        y_pred = sigmoid(predicted_linear_output)
        class_predictions = [0 if y<0.5 else 1 for y in y_pred]    # converting probabilities to class labels
        return class_predictions
    
l1 = LogisticRegression(learning_rate=0.01, num_iterations=1000)
X_test = np.array([
    [22, 20000],   # young, low salary
    [35, 120000],  # older, high salary
    [28, 30000],   # middle
    [50, 90000],   # older, high salary
])
y = np.array([0, 0, 1, 1])
l1.fit(X_test, y)
predictions = l1.predict(X_test)
print(predictions)  # Output: [0, 0, 1, 1]