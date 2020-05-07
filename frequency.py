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
        with open(path_defects+'%s.csv' % product_id, newline='') as defects_data:
            output = [str() for line in defects_data.readlines() for s in line[:-1].split(',')]
            print(output)
            #data = list(csv.reader(defects_data))
            print("File Loaded")
    else:
        data = ""
        print("Nosaj thing")

    return data

#done

def statistics():
    #load file
    data = loadData()

    #break into array
    print(data)


    #apply statistics




class freq():
    statistics()