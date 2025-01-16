import numpy as np
import matplotlib.pyplot as plt

number = np.random.normal(3000,1000, 1000)
plt.hist(number, bins=100)
plt.show()
print(number)