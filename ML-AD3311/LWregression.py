import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('tips.csv')
features = np.array(df['total_bill'])
labels = np.array(df['tip'])
def kernel(data, point, xmat, k):
    m, n = np.shape(xmat)
    ws = np.mat(np.eye(m))  
    for j in range(m):
        diff = point - xmat[j]
        ws[j, j] = np.exp(diff * diff.T / (-2.0 * k**2))
    return ws
def local_weight(data, point, xmat, ymat, k):
    wei = kernel(data, point, xmat, k)
    return (xmat.T * (wei * xmat)).I * (xmat.T * (wei * ymat.T))
def local_weight_regression(xmat, ymat, k):
    m, n = np.shape(xmat)
    ypred = np.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i] * local_weight(xmat, xmat[i], xmat, ymat, k)
    return ypred
m = features.shape[0]
mtip = np.mat(labels)
data = np.hstack((np.ones((m, 1)), np.mat(features).reshape(-1, 1)))
ypred = local_weight_regression(data, mtip, 0.5)
indices = data[:, 1].argsort(0)
xsort = data[indices][:, 0]
ysort = ypred[indices]
plt.figure(figsize=(10, 6))
plt.scatter(features, labels, color='blue', label='Actual')
plt.plot(xsort[:, 1], ysort, color='red', linewidth=3, label='LWLR Prediction')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Locally Weighted Linear Regression (LWLR)')
plt.legend()
plt.show()
