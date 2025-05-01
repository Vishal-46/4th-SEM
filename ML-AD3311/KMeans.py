import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.read_csv(r'driverdata.csv')
df = pd.DataFrame(data)
print(df)
col1 = df['Distance_Feature']
col2 = df['Speeding_Feature']
print(list(zip(col1, col2)))
X = np.array(list(zip(col1, col2)))
plt.xlim([0, 100])
plt.ylim([0, 50])
plt.title('Dataset')
plt.ylabel('Speeding_Feature')
plt.xlabel('Distance_Feature')
plt.scatter(col1, col2)
plt.show()
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']
kmeans_model = KMeans(n_clusters=3, random_state=0).fit(X)
for i, label in enumerate(kmeans_model.labels_):
    plt.plot(col1[i], col2[i], color=colors[label], marker=markers[label], ls='None')
plt.xlim([0, 100])
plt.ylim([0, 50])
plt.show()
