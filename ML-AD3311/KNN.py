import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
y = pd.DataFrame(iris.target, columns=['Targets'])
model = KMeans(n_clusters=3, random_state=0)
model.fit(X)
colormap = np.array(['red', 'lime', 'black'])
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Real Classification')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.subplot(1, 2, 2)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('KMeans Classification')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()
scaler = preprocessing.StandardScaler()
xsa = scaler.fit_transform(X)
xs = pd.DataFrame(xsa, columns=X.columns)
