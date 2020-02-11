# importing libraries 
import os, os.path 
  
# using the given path 
path = os.path.expanduser('~/nltk_data') 
  
# checking 
if not os.path.exists(path): 
    os.mkdir(path)
    print ("Does path exists : ", os.path.exists(path))

else:
    print("Folder already exists")

import nltk.data 
print ("\nDoes path exists in nltk : ",  
       path in nltk.data.path) 
