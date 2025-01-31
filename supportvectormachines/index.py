from sklearn import svm, datasets
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def createClusturedData(N, k):
    np.random.seed(1234)
    pointsPerCluster = float(N) / k
    X = []
    Y = []
    for i in range(k):
        incomeCentroid = np.random.uniform(20000, 200000)
        ageCentroid = np.random.uniform(20, 70)

        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000),
                     np.random.normal(ageCentroid, 2)])
            Y.append(i)

    X = np.array(X)
    Y = np.array(Y)
    return X, Y


(X, Y) = createClusturedData(100, 5)
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=Y.astype(float))


scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X)
X = scaling.transform(X)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=Y.astype(float))


C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X, Y)


def plotPredictions(clf):
    xx, yy = np.meshgrid(np.arange(-1, 1, .001), np.arange(-1, 1, .001))

    npx = xx.ravel()
    npy = yy.ravel()

    samplePoints = np.c_[npx, npy]

    Z = clf.predict(samplePoints)

    plt.figure(figsize=(8, 6))
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=Y.astype(float))
    plt.show()


plotPredictions(svc)
