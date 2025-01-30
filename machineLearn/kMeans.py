import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale


def createClusteredData(N, k):
    np.random.seed(10)
    pointsPerCluster = float(N) / k
    X = []
    for i in range(k):
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        ageCentroid = np.random.uniform(18, 80)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0),
                     np.random.normal(ageCentroid, 2.0)])

    X = np.array(X)
    return X


data = createClusteredData(100, 5)

model = KMeans(n_clusters=2)

model = model.fit(scale(data))


plt.figure(figsize=(8, 6))
plt.scatter(x=data[:, 0], y=data[:, 1], c=model.labels_.astype(float))
plt.show()
