from collections import Counter
from datas import age_income_activity, activity_score

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb

x_train, x_test, y_train, y_test = train_test_split(
    age_income_activity, activity_score, test_size=0.2, random_state=0)

train = xgb.DMatrix(x_train, label=y_train)
test = xgb.DMatrix(x_test, label=y_test)

params = {
    'max-depth': 4,
    'eta': 0.1,
    'objective': 'multi:softmax',
    'num_class': 3
}

epochs = 20

model = xgb.train(params, train, epochs)
predictions = model.predict(test)
print(predictions)
print(accuracy_score(y_test, predictions))

print(Counter(y_train))  # Her sınıfın kaç kez geçtiğini gör
