import numpy as np
import pandas as pd

from texts import english, turkish

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.DataFrame({'message': [], 'language': []})


def addToArrays(data, texts, language):
    rows = [{'message': text, 'language': language} for text in texts]
    return pd.concat([data, pd.DataFrame(rows)], ignore_index=True)


data = addToArrays(data, english, 'English')
data = addToArrays(data, turkish, 'Turkish')

vectorizer = CountVectorizer()
count = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['language'].values

classifier.fit(count,targets)

examples = ['Merhaba Ben Murat','hello my name is murat','Sakız Çiğnedim']
exampleCounts = vectorizer.transform(examples)
predictions = classifier.predict(exampleCounts)
print(predictions)


