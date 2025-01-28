import yfinance as yf
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = yf.download('GOOGL', start='2020-01-01', end='2023-01-01')

df['HlPercentage'] = (df['High'] - df['Close']) / df['Close'] * 100.0
df['Percentage'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

df = df[['Close', 'HlPercentage', 'Percentage', 'Volume']]

forecast_col = 'Close'
df.fillna(-9999, inplace=True)

forecast_out = int(math.ceil(0.1 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['label'], axis=1))
y = np.array(df['label'])
X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)
