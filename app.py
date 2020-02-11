#  Version 1.0 Springboard defects classifier 
# API https://www.amazon.com/reviews/iframe?akid=[AWS Access Key ID]&asin=0316067938&exp=2011-08-01T17%3A54%3A07Z&linkCode=xm2&summary=0&tag=ws&truncate=256&v=2&sig=[Signature]

#Imports 

import os
import json

import re
import nltk
import numpy as np
import pandas as pd

from classifier import dictionaryCheck
from vocabulary import Vocabulary
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


print("Welcome to springboard defects classifier")


#Get and load data into these arrays 
sample = "i am a  huge fan of the iphone 10. it is an amazing product created by samsung and i hate microsoft"
product_id = "0528881469"
review_text = ""
reviewDefects = ["Heating", "update", "battery"] 

#Functions 
def loadData():
    with open('sample.json') as json_data:
        data = json.load(json_data)
        for r in data["Chunk"]:
            print(r["reviewText"])

def caseConvert():
    for text in sample:
        sample_cased = text.lower()
        print(sample_cased)
    print("set converted")

def tokenize():
    #Tokenize
    sample_token = word_tokenize(sample)
    sample_token

    #Remove stop words
    swords = set(stopwords.words('english'))
    filtered_sentence = [word for word in sample_token if word not in swords]
    filtered_sentence = [] 

def sentimentCheck(): 
    blob = TextBlob(sample)
    blobP = blob.sentiment.polarity
    blobS = blob.sentiment.subjectivity
    print(blob.sentiment)

if blob.sentiment.polarity < 0.075:
    #Run Dictionary search
    dictionaryCheck()
    print("Analyzing")
else:
  print("Chunk is clean") 

def writeBlob():
    with open('%s.json' % product_id,'a') as saveFile:
        saveFile.write("{")
        saveFile.write(json.dumps("review_text :" + sample))
        saveFile.write(json.dumps("review_polarity :" + str(blobP)))
        saveFile.write(json.dumps("review_subjectivity :" + str(blobS)))
        saveFile.write(json.dumps("review_defects :" + str(reviewDefects)))
        saveFile.write("},")
        saveFile.write("\n")
        saveFile.close()

#Run class

class app():

    loadData()
    caseConvert()
    tokenize()
    sentimentCheck()
    writeBlob()