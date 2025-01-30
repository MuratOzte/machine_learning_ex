from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas

import xgboost as xgb

iris = load_iris()

df = iris.data
print(df)

numSamples, numFeatures = iris.data.shape

x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=0)

train = xgb.DMatrix(x_train, label=y_train)
test = xgb.DMatrix(x_test, label=y_test)

print(train)

params = {
    'max-depth': 4,
    'eta': 0.3,
    'objective': 'multi:softmax',
    'num_class': 3
}
epochs = 10

model = xgb.train(params,train,epochs)
predictions = model.predict(test)
print(predictions)

print(accuracy_score(y_test,predictions))
