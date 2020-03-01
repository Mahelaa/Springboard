import os
import json

product_id = "0528881469"

#Open file
#Functions
def loadData():
    with open('sample.json') as json_data:
        data = json.load(json_data)
        for r in data["Chunk"]:
            print(r["reviewText"])

#Read Data

#Generate report
#Read frequency

#Output
if product == severe:
    print("Product ",product_id, "has faults")
    print(faults)
else:
    print("Your product has only minor issues")

