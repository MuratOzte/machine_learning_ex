import os
import io
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath): 
            with io.open(filepath, 'r', encoding='latin1', errors='ignore') as f:
                message = f.read()
            yield filepath, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)
    return pd.DataFrame(rows, index=index)


data = pd.DataFrame({'message': [], 'class': []})

data = pd.concat([data, dataFrameFromDirectory(
    "./emailSpamControl/emails/ham", "ham")])
data = pd.concat([data, dataFrameFromDirectory(
    "./emailSpamControl/emails/spam", "spam")])


vectorizer = CountVectorizer()
count = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values

classifier.fit(count,targets)

examples = ['Free Ticket now!!!', "Hi Bob, how about a game of golf tomorrow?"]

example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(predictions)

