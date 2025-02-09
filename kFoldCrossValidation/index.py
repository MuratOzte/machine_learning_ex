import numpy as np
import sklearn
from sklearn import datasets
from sklearn import model_selection
from sklearn import svm

iris = datasets.load_iris()

x_train, x_test, y_train, y_test = model_selection.train_test_split(
    iris.data, iris.target, test_size=0.4, random_state=0)

clf = svm.SVC(kernel='linear', C=1).fit(X=x_train, y=y_train)
score = clf.score(X=x_test, y=y_test)

crossvalScore = model_selection.cross_val_score(clf,iris.data,iris.target,cv=5)
print(crossvalScore)
print(crossvalScore.mean())