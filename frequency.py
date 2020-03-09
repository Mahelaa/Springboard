import os
import json
import os.path
from os import path
import pandas as pd

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
    print(pd.Series(data).value_counts())



#Read Data

class freq():
    statistics()