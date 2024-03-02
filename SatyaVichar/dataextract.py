import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string
from sklearn. feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

DT = DecisionTreeClassifier()
vectorization = TfidfVectorizer()

class Everything:
    def __init__(self, fake_data, true_data):
        print("Called")
        self.fake_data = fake_data
        self.true_data = true_data

        self.fake_data["class"] = 0
        self.true_data["class"] = 1

        print(self.true_data.head(10))

        merged_data = pd.concat([self.fake_data, self.true_data])

        data = merged_data

        data = data.sample(frac=1)

        data.reset_index(inplace=True)
        #data.drop(['index'], axis=1, inplace=True)

        def cleaning(text):
            if pd.isnull(text):  # Check for NaN values
                return ""
            #text = text.lower()
            text = re.sub('\[ .*? \]', '', text)
            text = re.sub("\\W", " ", text)
            text = re.sub('https ?: //\S+|www\.\S+', '', text)
            text = re.sub(' <.*? >+', '', text)
            text = re.sub(' [%s]' % re. escape(string.punctuation), '', text)
            text = re.sub('\n', '', text)
            text = re.sub('\w*\d\w*', '', text)
            return text

        data['text'] = data['text'].apply(cleaning)

        x = data['text']
        y = data['class']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

        
        xv_train = vectorization.fit_transform(x_train)
        xv_test = vectorization.transform(x_test)

        DT.fit(xv_train, y_train)

        print("Called2")

# pred_dt = DT.predict(xv_test)
# # print(pred_dt)
# print(DT.score(xv_test, y_test))

    def manual_testing(self, news):
        testing_news = {"text": [news]}
        new_def_test = pd.DataFrame(testing_news)

        def cleaning(text):
            #text = text.lower()
            text = re.sub('\[ .*? \]', '', text)
            text = re.sub("\\W", " ", text)
            text = re.sub('https ?: //\S+|www\.\5+', '', text)
            text = re.sub(' <.*? >+', '', text)
            text = re.sub(' [%s]' % re. escape(string.punctuation), '', text)
            text = re.sub('\n', '', text)
            text = re.sub('\w*\d\w*', '', text)
            return text

        new_def_test["text"] = new_def_test["text"].apply(cleaning)

        new_x_test = new_def_test["text"]
        new_xv_test = vectorization.transform(new_x_test)

        pred_DT = DT.predict(new_xv_test)

        if (pred_DT[0]==0):
            return "Fake News"
        elif (pred_DT[0]==1):
            return "Not Fake"


# while(True):
#     news = str(input())
#     print(obj.manual_testing(news))




