import numpy as np
import matplotlib.pyplot as plt


def de_mean(x):
    return np.mean(x)


def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y) / (n-1))


pageSpeed = np.random.normal(3, 1, 1000)
purchaseAmount = np.random.normal(50, 10, 1000)

print(np.corrcoef(pageSpeed, purchaseAmount))
print(np.cov(pageSpeed, purchaseAmount))

plt.scatter(x=pageSpeed, y=purchaseAmount)
plt.show()
