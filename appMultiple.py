# Version 1.0 Springboard defects classifier
# API https://www.amazon.com/reviews/iframe?akid=[AWS Access Key ID]&asin=0316067938&exp=2011-08-01T17%3A54%3A07Z&linkCode=xm2&summary=0&tag=ws&truncate=256&v=2&sig=[Signature]

#Imports 

import os
import json
import os.path
import time

import re
import nltk
import numpy as np
import pandas as pd
import csv

from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


print("Welcome to springboard defects classifier")
start_time = time.time()
#time.sleep(5)
defects_list = []
product_id_file = ""
dataset_loop = 0

#Functions
def loadData():
    #set input statement
    with open('./Corpus/Springboard/sample.json') as json_data:
        sample = json.load(json_data)
        description = sample['Chunk'][dataset_loop]['reviewText']
        #Alter this to take in datasets

    return description

def loadData2():
    #set input statement
    with open('./Corpus/Springboard/sample.json') as json_data:
        sample = json.load(json_data)
        product_id_file = sample['Chunk'][dataset_loop]['asin']

    return product_id_file

def caseConvert():
    sample = loadData()
    sample_cased = sample.lower()
    print("Text converted")

    return sample_cased


def tokenize():
    sample_cased = caseConvert()
    #Tokenize
    sample_token = word_tokenize(sample_cased)
    sample_token

    #Remove stop words
    swords = set(stopwords.words('english'))
    filtered_sentence = [word for word in sample_token if word not in swords]
    print(filtered_sentence)

    return filtered_sentence

def sentimentCheck():
    sample_cased = caseConvert()

    blob = TextBlob(sample_cased)

    return blob

def dictionaryCheck():
    with open('/Users/terminus/Github/Springboard/Corpus/Springboard/defects_electronics', 'r') as f:
        corpus = f.read().splitlines()

    sample_token = tokenize()

    #dictionary check and classify
    for word in sample_token:
        if(word in corpus):
            defects_list.append(word)
        else:
            print("No Matches")

    print(defects_list)
    return defects_list

def writeBlob():
    #
    blob = sentimentCheck()
    defects_list = dictionaryCheck()
    sample = loadData()
    product_id_file = loadData2()

    blobP = blob.sentiment.polarity
    blobS = blob.sentiment.subjectivity

    directory = './defects/'
    filename =  ('%s.csv' % product_id_file)

    file_path = os.path.join(directory, filename)
    #change condition to check file
    if not os.path.isdir(directory):
        os.mkdir(directory)
        with open(file_path, mode='w') as defects_write:
            defects_append= csv.writer(defects_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            defects_append.writerow(defects_list)
            print("New file created!")
    else:
        with open(file_path, mode='a') as defects_write:
            defects_append= csv.writer(defects_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            defects_append.writerow(defects_list)
            print("Product defects appended")


#Run class

class app():

    while dataset_loop < 10:

        loadData()
        caseConvert()
        tokenize()
        sentimentCheck()
        dictionaryCheck()
        writeBlob()
        dataset_loop+=1

    print("--- %s seconds ---" % (time.time() - start_time))