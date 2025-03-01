import numpy as np  # Importing NumPy for mathematical operations

# Define the sigmoid activation function
def sigmoid(x):
    """
    Sigmoid function: f(x) = 1 / (1 + e^(-x))
    Used to squash values between 0 and 1.
    """
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    """
    Derivative of the sigmoid function.
    This is used for backpropagation to update weights.
    """
    return x * (1 - x)

# Define input dataset (XOR problem)
X = np.array([[0, 0],  
              [0, 1],  
              [1, 0],  
              [1, 1]])  # Input features (2 inputs per sample)

# Define expected output dataset
y = np.array([[0],  # Output for [0,0]
              [1],  # Output for [0,1]
              [1],  # Output for [1,0]
              [0]]) # Output for [1,1]

# Set random seed for reproducibility
np.random.seed(1)

# Initialize weights and biases randomly
weights_input_hidden = np.random.uniform(size=(2, 2))  # 2 neurons in hidden layer
weights_hidden_output = np.random.uniform(size=(2, 1))  # 1 neuron in output layer
bias_hidden = np.random.uniform(size=(1, 2))  # Bias for hidden layer (2 neurons)
bias_output = np.random.uniform(size=(1, 1))  # Bias for output layer (1 neuron)

# Define training parameters
epochs = 10000  # Number of iterations for training
learning_rate = 0.1  # Speed of learning (adjusting weights)

# Training the neural network
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden  # Calculate hidden layer input
    hidden_layer_output = sigmoid(hidden_layer_input)  # Apply activation function
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output  # Calculate output layer input
    predicted_output = sigmoid(output_layer_input)  # Apply activation function
    
    # Calculate error
    error = y - predicted_output  # Difference between actual and predicted output
    
    # Backpropagation
    d_predicted_output = error * sigmoid_derivative(predicted_output)  # Calculate gradient for output layer
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)  # Backpropagate error to hidden layer
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)  # Calculate gradient for hidden layer
    
    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate  # Update weights for output layer
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate  # Update bias for output layer
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate  # Update weights for hidden layer
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate  # Update bias for hidden layer
    
    # Print error every 1000 epochs to monitor training progress
    if epoch % 1000 == 0:
        print(f"Epoch {epoch} Error: {np.mean(np.abs(error))}")

# Final output after training
print("\nFinal Output after Training:")
print(predicted_output)
