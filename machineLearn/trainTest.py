import numpy as np
import pylab as plb
from rsqu import r_squared

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds


# %80 train %20 test
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

x = np.array(trainX)
y = np.array(trainY)

p4 = np.poly1d(np.polyfit(x, y, 6))

# train data
xp = np.linspace(0, 7, 1000)
axes = plb.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plb.scatter(testX, testY)
plb.plot(xp, p4(xp), c='r')

y_pred = p4(testX)

r2 = r_squared(testY, y_pred)

# r2 = r_squared(testY, y_pred)
print(f"R-kare (R-squared) değeri: {r2}")
