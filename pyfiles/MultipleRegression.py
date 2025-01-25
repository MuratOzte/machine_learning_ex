import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Veriyi oku
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

# İlgili sütunları seç
df1 = df[['Mileage', 'Price']]

# Eksik verileri temizle
df1 = df1.dropna()

# Gruplama için aralıkları belirle
bins = np.arange(0, 50000, 10000)

# Mileage sütununa göre grupla ve ortalama fiyatları hesapla
groups = df1.groupby(pd.cut(df1['Mileage'], bins)).mean()

# Grupları yazdır
print(groups.head())

# Grafiği çiz
plt.plot(groups.index.astype(str), groups['Price'])
plt.xlabel('Mileage Groups')
plt.ylabel('Average Price')
plt.title('Average Price by Mileage Group')
plt.xticks(rotation=45)


X = df[['Mileage', 'Cylinder', 'Doors']]
Y = df[['Price']]

