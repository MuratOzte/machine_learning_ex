from sklearn.ensemble import RandomForestClassifier
import pydotplus
from io import StringIO
from IPython.display import Image, display
import pandas as pd
import numpy as np
from sklearn import tree

filePath = "./cvFilter/PastHires.csv"

df = pd.read_csv(filePath, header=0)

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)

features = list(df.columns[:6])

y = df['Hired']
x = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

print(clf.tree_)

dotData = StringIO()
tree.export_graphviz(clf, out_file=dotData, feature_names=features)
graph = pydotplus.graph_from_dot_data(dotData.getvalue())
graph.write_png("./cvFilter/tree.png")
display(Image(graph.create_png()))

clf = RandomForestClassifier(n_estimators=10)
clf.fit(x, y)

print(clf.predict([[10, 1, 4, 0, 0, 0]]))
print(clf.predict([[10, 0, 4, 0, 0, 0]]))
