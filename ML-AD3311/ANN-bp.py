# Import the numpy library for matrix operations
import numpy as np
# numpy (np) is a library that makes math operations (like multiplication of matrices) fast and easy.
# We use it for all calculations in the neural network.

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# This function takes any number (x) and squashes it between 0 and 1.
# Example: sigmoid(-10) ≈ 0, sigmoid(0) = 0.5, sigmoid(10) ≈ 1.
# We use it to make the network's predictions smooth and interpretable.

# Derivative of sigmoid (used in backpropagation)
def sigmoid_derivative(x):
    return x * (1 - x)
# This calculates the "slope" of the sigmoid function at a given point.
# It’s used during backpropagation to figure out how much to adjust weights.
# Example: if x = 0.5, then sigmoid_derivative(0.5) = 0.5 * (1 - 0.5) = 0.25.

# Our dataset
X = np.array([[2, 3],  # Hours Studied, Hours Slept
              [4, 5],
              [1, 2],
              [6, 7]])
# X is the input data: each row is one example, each column is a feature.
# Here, we have 4 examples with 2 features: Hours Studied and Hours Slept.
# Shape of X is (4, 2) meaning 4 rows, 2 columns.

y = np.array([[0],     # Pass (0 = fail, 1 = pass)
              [1],
              [0],
              [1]])
# y is the target output: what we want the network to predict.
# 0 means "fail," 1 means "pass." Each row corresponds to a row in X.
# Shape of y is (4, 1).

# Initialize weights and biases randomly
np.random.seed(1)  # For reproducibility
# This sets a "seed" so random numbers are the same every time you run the code.
# It’s like rolling a die but always getting the same sequence of numbers.

input_size = 2     # 2 inputs
hidden_size = 2    # 2 hidden neurons
output_size = 1    # 1 output
# These define the structure of the network:
# - 2 inputs (Hours Studied, Hours Slept).
# - 2 neurons in the hidden layer (a middle step to process inputs).
# - 1 output (Pass or Fail).

weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
# Weights between input layer and hidden layer.
# Shape is (2, 2): 2 inputs connecting to 2 hidden neurons.
# Random values between 0 and 1 are assigned (e.g., [[0.42, 0.65], [0.15, 0.32]]).

weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))
# Weights between hidden layer and output layer.
# Shape is (2, 1): 2 hidden neurons connecting to 1 output neuron.
# Random values like [[0.78], [0.23]].

bias_hidden = np.zeros((1, hidden_size))
# Bias for the hidden layer, starts as zeros.
# Shape is (1, 2): one bias per hidden neuron, e.g., [[0, 0]].
# Bias helps shift the activation function.

bias_output = np.zeros((1, output_size))
# Bias for the output layer, starts as zeros.
# Shape is (1, 1): one bias for the output neuron, e.g., [[0]].

# Training parameters
learning_rate = 0.1
# How fast the network adjusts its weights. Small steps (0.1) are safe for beginners.
# Too big (e.g., 10) might overshoot, too small (e.g., 0.001) might take forever.

epochs = 1000  # Number of iterations
# How many times the network sees the full dataset to learn.
# 1000 iterations gives it enough time to adjust weights.

# Training the network (Backpropagation)
for epoch in range(epochs):
    # Loop over the dataset 1000 times to train the network.
    
    # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    # Calculate input to the hidden layer.
    # X (4, 2) * weights_input_hidden (2, 2) = (4, 2), then add bias_hidden (1, 2).
    # Example: For [2, 3], might get [[1.5, 2.1]] after dot product and bias.
    
    hidden_layer_output = sigmoid(hidden_layer_input)
    # Apply sigmoid to squash hidden layer inputs to 0-1 range.
    # Example: [[1.5, 2.1]] becomes [[0.82, 0.89]].
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    # Calculate input to the output layer.
    # hidden_layer_output (4, 2) * weights_hidden_output (2, 1) = (4, 1), then add bias.
    # Example: [[0.82, 0.89]] might become [[1.2]].
    
    predicted_output = sigmoid(output_layer_input)
    # Apply sigmoid to get final predictions between 0 and 1.
    # Example: [[1.2]] becomes [[0.77]].
    
    # Calculate error
    error = y - predicted_output
    # Difference between target (y) and prediction.
    # Shape is (4, 1). Example: if y = [[0]] and predicted = [[0.77]], error = [[-0.77]].
    
    # Backpropagation
    output_delta = error * sigmoid_derivative(predicted_output)
    # How much to adjust the output layer weights.
    # Multiply error by the slope of sigmoid at predicted_output.
    # Example: -0.77 * sigmoid_derivative(0.77) ≈ -0.77 * 0.18 = -0.14.
    
    hidden_error = np.dot(output_delta, weights_hidden_output.T)
    # Propagate the error back to the hidden layer.
    # output_delta (4, 1) * weights_hidden_output.T (1, 2) = (4, 2).
    # This tells us how much the hidden layer contributed to the error.
    
    hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)
    # How much to adjust hidden layer weights.
    # Multiply hidden_error by the slope of sigmoid at hidden_layer_output.
    
    # Update weights and biases
    weights_hidden_output += learning_rate * np.dot(hidden_layer_output.T, output_delta)
    # Adjust weights between hidden and output layers.
    # hidden_layer_output.T (2, 4) * output_delta (4, 1) = (2, 1), scaled by learning_rate.
    
    weights_input_hidden += learning_rate * np.dot(X.T, hidden_delta)
    # Adjust weights between input and hidden layers.
    # X.T (2, 4) * hidden_delta (4, 2) = (2, 2), scaled by learning_rate.
    
    bias_output += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    # Update output bias by summing output_delta and scaling by learning_rate.
    
    bias_hidden += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)
    # Update hidden bias by summing hidden_delta and scaling by learning_rate.
    
    # Print error every 100 epochs
    if epoch % 100 == 0:
        loss = np.mean(np.square(error))
        # Loss is the average squared error across all examples.
        # Tells us how far off the predictions are. Lower is better.
        print(f"Epoch {epoch}, Loss: {loss}")

# Test the network and print Pass/Fail
print("\nFinal Predictions:")
test_output = sigmoid(np.dot(sigmoid(np.dot(X, weights_input_hidden) + bias_hidden), weights_hidden_output) + bias_output)
# Run the forward pass again to get final predictions after training.
# Same steps as above, but using the trained weights and biases.

# Threshold for Pass/Fail (0.5)
for i in range(len(X)):
    # Loop through each example in the dataset.
    hours_studied = X[i][0]
    hours_slept = X[i][1]
    # Get the input values for this example (e.g., 2 and 3).
    prediction = test_output[i][0]
    # Get the predicted value (e.g., 0.1234).
    result = "Pass" if prediction >= 0.5 else "Fail"
    # If prediction ≥ 0.5, call it "Pass"; otherwise, "Fail".
    print(f"Hours Studied: {hours_studied}, Hours Slept: {hours_slept} -> Prediction: {prediction:.4f} -> {result}")
# Print the inputs, predicted value (rounded to 4 decimals), and Pass/Fail result.