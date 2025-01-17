import numpy as np
import matplotlib.pyplot as plt

age = np.random.randint(high=80, low=18, size=1000)
timeSpent = np.random.randint(low=20, high=800, size=1000)

plt.scatter(age, timeSpent)
plt.xlabel("age")
plt.ylabel("time spent")
plt.title("Age vs Time spent on tv")
plt.show()
