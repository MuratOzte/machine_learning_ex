import matplotlib.pylab as plb
import numpy as np

np.random.seed(2)
pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeeds

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))
xp = np.linspace(0, 7, 100)

plb.plot(xp, p4(xp), c='r')


plb.scatter(pageSpeeds, purchaseAmount)
plb.show()
