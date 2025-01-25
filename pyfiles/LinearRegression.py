import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmount = 50 - (3 * (pageSpeeds + np.random.normal(0, 0.1, 1000)))

plt.scatter(pageSpeeds, purchaseAmount)

slope, intercept, r_value, p_value, std_error = stats.linregress(
    pageSpeeds, purchaseAmount)

print(r_value ** 2)


def predict(x):
    return slope * x + intercept


fitline = predict(pageSpeeds)
plt.plot(pageSpeeds, fitline, c='r')
plt.show()
