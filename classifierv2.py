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

sample = "We got this GPS for my husband who is an (OTR) over the road trucker.  Very Impressed with the shipping time, it arrived a few days earlier than expected...  within a week of use however it started freezing up... could of just been a glitch in that unit.  Worked great when it worked!  Will work great for the normal person as well but does have the \"trucker\" option. (the big truck routes - tells you when a scale is coming up ect...)  Love the bigger screen, the ease of use, the ease of putting addresses into memory.  Nothing really bad to say about the unit with the exception of it freezing which is probably one in a million and that's just my luck.  I contacted the seller and within minutes of my email I received a email back with instructions for an exchange! VERY impressed all the way around!"

#import custom bof model and use to build vocabulary
data = pd.read_csv("/Users/terminus/Github/Springboard/defects_voc.tsv", delimiter="\t")
print(data)
data.head()


#split the dataset to manageable chunks
def simple_split(data,y,length,split_mark=0.7):
    if split_mark > 0. and split_mark < 1.0:
        n = int(split_mark*length)
    else:
        n = int(split_mark)
    x_train = data[:n].copy()
    x_test = data[n:].copy()
    y_train = y[:n].copy()
    y_test = y[n:].copy()
    return x_train,x_test,y_train,y_test

#use to train and test
vectorizer = CountVectorizer()

x_train,x_test,y_train,y_test = simple_split(data.severity,data.fields,len(data))
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
print(x_train)

logreg = LogisticRegression()
nb = MultinomialNB()
rf = RandomForestClassifier()

#Fit model

logreg = LogisticRegression()
logreg.fit(x_train, y_train)
print("Training set score: {:.3f}".format(logreg.score(x_train, y_train)))
print("Test set score: {:.3f}".format(logreg.score(x_test, y_test)))

nb = MultinomialNB()
nb.fit(x_train, y_train)
print("Training set score: {:.3f}".format(nb.score(x_train, y_train)))
print("Test set score: {:.3f}".format(nb.score(x_test, y_test)))

rf = RandomForestClassifier()
rf.fit(x_train, y_train)
print("Training set score: {:.3f}".format(rf.score(x_train, y_train)))
print("Test set score: {:.3f}".format(rf.score(x_test, y_test)))

print(logreg.predict(vectorizer.transform([sample]))[0])
print(rf.predict(vectorizer.transform([sample]))[0])
print(nb.predict(vectorizer.transform([sample]))[0])

#Output
