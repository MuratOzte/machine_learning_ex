from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as plb
from itertools import cycle

iris = load_iris()

num_samples, num_features = iris.data.shape

x = iris.data
pca = PCA(n_components=2, whiten=True).fit(x)
x_pca = pca.transform(x)

colors = cycle('rgb')
target_ids = range(len(iris.target_names))
plb.figure()

for i, c, label in zip(target_ids, colors, iris.target_names):
    plb.scatter(x_pca[iris.target == i, 0],
                x_pca[iris.target == i, 1], c=c, label=label)
    
plb.legend()
plb.show()
