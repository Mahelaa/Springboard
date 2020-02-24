import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier


#Load Corpus
with open('/Users/terminus/Github/Springboard/Corpus/Springboard/defects_electronics', 'r') as f:
    corpus = f.read().splitlines()
phrases=["the quick brown fox is not gay",
"hello from the other side, my name is jame charle"]

vect= CountVectorizer()
vect.fit(phrases)

print("Vocabulary size: {} ".format(len(vect.vocabulary_)))
print("Vocabulary content:\n {} ".format(vect.vocabulary_))

bag_of_words = vect.transform(phrases)
print(bag_of_words)

print("bagofwords as an array: \n {}" .format(bag_of_words.toarray()))

vect.get_feature_names()

sample = "We got this GPS for my husband who is an (OTR) over the road trucker.  Very Impressed with the shipping time, it arrived a few days earlier than expected...  within a week of use however it started freezing up... could of just been a glitch in that unit.  Worked great when it worked!  Will work great for the normal person as well but does have the \"trucker\" option. (the big truck routes - tells you when a scale is coming up ect...)  Love the bigger screen, the ease of use, the ease of putting addresses into memory.  Nothing really bad to say about the unit with the exception of it freezing which is probably one in a million and that's just my luck.  I contacted the seller and within minutes of my email I received a email back with instructions for an exchange! VERY impressed all the way around!"

data = pd.read_csv("Sample Data/labeledTrainData.tsv", delimiter="\t")
print(data)
data.head()

print("Samples per class: {}".format(np.bincount(data.sentiment)))

def simple_split(data,y,length,split_mark=0.7):
    if split_mark > 0. and split_mark < 1.0:
        n = int(split_mark*length)
    else:
        n = int(split_mark)
    X_train = data[:n].copy()
    X_test = data[n:].copy()
    y_train = y[:n].copy()
    y_test = y[n:].copy()
    return X_train,X_test,y_train,y_test

vectorizer = CountVectorizer()

x_train,x_test,y_train,y_test = simple_split(data.review,data.sentiment,len(data))
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

print("Samples per class: {}".format(np.bincount(y_train)))
print("Samples per class: {}".format(np.bincount(y_test)))

x_train = vectorizer.fit_transform(x_train)
x_test = vectorizer.fit_transform(x_test)

feature_names = vectorizer.get_feature_names()
print("Number of features: {}".format(len(feature_names)))
print("First 20: {}".format(feature_names[:20]))
print("Features 19500 to 19530: {}".format(feature_names[19500:19530]))
print("Every 2000th Feature: {}".format(feature_names[::2000]))

vectorizer.vocabulary_