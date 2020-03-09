import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

global defects_list = []

def dictionaryCheck(sample_token):
    with open('/Users/terminus/Github/Springboard/Corpus/Springboard/defects_electronics', 'r') as f:
        corpus = f.read().splitlines()

    #Remove StopWords
    for word in sample_token:
        if(word in corpus):
            print ("Element Exists")
            print(word)
            defects_list.append(word)
        else:
            print("Non Match")

    print(defects_list)
    return defects_list

