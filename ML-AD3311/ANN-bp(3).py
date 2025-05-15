import numpy as np

# Input and Output
X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)  # Input: Hours Studied, Hours Slept
y = np.array([[92], [86], [89]], dtype=float)        # Output: Test scores

# Normalize input and output
X = X / np.amax(X, axis=0)   # Normalize input features
y = y / 100                  # Normalize output

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network Architecture
epoch = 5000        # Number of training iterations
lr = 0.1            # Learning rate
inputlayer_neurons = X.shape[1]     # 2 features
hiddenlayer_neurons = 3
output_neurons = 1

# Weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))  # Weights Input-Hidden
bh = np.random.uniform(size=(1, hiddenlayer_neurons))                   # Bias Hidden
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))    # Weights Hidden-Output
bout = np.random.uniform(size=(1, output_neurons))                      # Bias Output

# Training loop
for i in range(epoch):
    # Forward Pass
    hlayer_input = np.dot(X, wh) + bh
    hlayer_act = sigmoid(hlayer_input)

    output_input = np.dot(hlayer_act, wout) + bout
    output = sigmoid(output_input)

    # Backpropagation
    EO = y - output                   # Error at output
    outgrad = sigmoid_derivative(output)
    d_output = EO * outgrad

    EH = d_output.dot(wout.T)        # Error at hidden layer
    hiddengrad = sigmoid_derivative(hlayer_act)
    d_hiddenlayer = EH * hiddengrad

    # Update Weights and Biases
    wout += hlayer_act.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

    # Print every 1000 epochs
    if i % 1000 == 0:
        print(f"Epoch {i}")
        print("Predicted Output:\n", output)
        print("Loss:", np.mean(np.square(y - output)))
        print("--------------")

# Final Output
print("Final Predicted Output:\n", output * 100)  # Scale back to 0-100
