import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100,20,1000)
plt.hist(incomes,20)
plt.show()

stddev = incomes.std()
variance = incomes.var()
print(stddev,variance)