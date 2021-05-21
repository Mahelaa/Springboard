import os
import json
import os.path
from os import path
import pandas as pd
import csv
import collections
import csv
from collections import Counter
from collections import defaultdict

sample_id = "0528881469"
results = []

def getFile():
    #Open File from input
    product_id_input = input ("Enter a product id: ")

    print("OPENING FILE")
    return product_id_input


#Functions
def loadData():
    product_id = getFile()
    path_defects = './defects/'


    if (path.exists(path_defects+'%s.csv' % product_id)):
        with open(path_defects+'%s.csv' % product_id , 'r') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            ctr = 0
            rows = 0
            word = 'heating'
            for row in reader:
                if word in row[1]:
                    rows += 1
                    ctr += row[1].count(word)
                    print(row)
            print('heating: {}, rows: {}'.format(ctr, rows))


            """ for word_individual_Sum in data:
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
    else:
        data = ""
        print("Nosaj thing")

    return data

#done

def statistics():
    data = loadData()
    #apply statistics

class freq():
    statistics()