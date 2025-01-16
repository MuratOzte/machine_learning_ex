import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

values = np.random.normal(10,0.5,10000)
plt.hist(values,30)

firstMoment = np.mean(values)
secondMoment = np.var(values)
thirdMoment = sp.skew(values)
forthMoment = sp.kurtosis(values)
print(firstMoment,secondMoment,thirdMoment,forthMoment )

plt.show()
