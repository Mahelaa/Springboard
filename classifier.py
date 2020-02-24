import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from vocabulary import Vocabulary

sample = "i am a  huge fan of the iphone 10. it is an amazing product created by samsung and i hate microsoft"

def dictionaryCheck():
    #Tokenize
    sample_token = word_tokenize(sample)
    sample_token

    #Remove stop words
    swords = set(stopwords.words('english'))
    filtered_sentence = [word for word in sample_token if word not in swords]
    print(filtered_sentence)

dictionaryCheck() 