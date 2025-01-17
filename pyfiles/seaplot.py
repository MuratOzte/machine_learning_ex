import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")

gear_counts = df['# Gears'].value_counts()

sb.set()

df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]

sb.lmplot(x="Eng Displ", y="CombMPG", data=df)
plt.show()