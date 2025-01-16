import numpy as np
import matplotlib.pyplot as plt

values = np.random.uniform(-10,10,10000)
# plt.hist(values,30)
# plt.show()

from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(-3,3,0.1)
plt.plot(x,norm.pdf(x))
plt.title = "Probility Density Form"
plt.xlabel = "Values"
plt.ylabel = "Probility density"
plt.show()

