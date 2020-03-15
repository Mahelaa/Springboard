import os
import json
import os.path
from os import path
import pandas as pd
from collections import Counter

sample_id = "0528881469"

def getFile():
    #Open File from input
    product_id_input = input ("Enter a product id: ")

    print("OPENING FILE")
    return product_id_input


#Functions
def loadData():
    product_id = getFile()

    path_defects = './defects/'
    if (path.exists(path_defects+'%s.txt' % product_id)):
        with open(path_defects+'%s.txt' % product_id, 'r') as defects_data:
            data = defects_data.read().splitlines()
            print("File Loaded")
    else:
        data = ""
        print("Nosaj thing")

    return data

def statistics():
    data = loadData()

    for word in data:
        word = word.replace('"', '')
        word_count = Counter(word.split())
        count_of_words_sum = sum(Counter(word_count).values())

        countValue = word_count('heating')

        print(word_count)

        """ #Get indivisual word
        for word_individual_Sum in data:
            #get individual value
            countValue = counter[word_individual_Sum]
            print(countValue)
            #for each words value
            for defect in word_count:
                percentage = countValue/count_of_words_sum
            if( percentage < 10):
                print("defect ", +defect, " is not severe @")
            elif(10 <= percentage <= 40):
                print("defect ", +defect, " is a mild defect")
            elif(percentage > 40):
                print("defect ", +defect, " is a severe failure rate")
            else:
                print("No data") """


class freq():
    statistics()