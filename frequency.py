import os
import json

product_id = "0528881469"


def getFile():
    #Open File
    product_id_input = input ("Enter a product id: ")
    product_id = int(product_id_input)

# Prints in the console the variable as requested
    print ("The product id is: ", product_id)
    print("OPENING FILE")


#Functions
def loadData():
    with open('%s.txt' % product_id) as json_data:
        data = json.load(json_data)
        for r in data["Chunk"]:
            print(r["reviewText"])

#Read Data

def statistics():

#Generate report
#Read frequency
#Output

    if product == severe:
        print("Product ",product_id, "has faults")
        print(faults)
    else:
        print("Your product has only minor issues")

    return severityIndex

class freq():
    getFile()