import numpy as np
import matplotlib.pyplot as plt

values = np.random.normal(0,0.5,1000)
plt.hist(values,30)
# plt.show()

perc = np.percentile(values,50)
print(perc*100, '%')