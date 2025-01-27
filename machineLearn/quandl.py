import yfinance as yf
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

df = yf.download('GOOGL', start='2020-01-01', end='2023-01-01')

df['HlPercentage'] = (df['High'] - df['Close']) / df['Close'] * 100.0
df['Percentage'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

df = df[['Close', 'HlPercentage', 'Percentage', 'Volume']]

forecast_col = 'Close'
df.fillna(-9999, inplace=True)

forecast_out = int(math.ceil(0.1 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
