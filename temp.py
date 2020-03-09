""" #Diffferent
def dictionaryCheckV2():
    with open('/Users/terminus/Github/Springboard/Corpus/Springboard/defects_electronics', 'r') as f:
        corpus = f.read().splitlines()
        print(corpus)

    #Tokenize
    sample_token = word_tokenize(sample)
    sample_token

    for word in sample_token:
        for defect in corpus:
            if(word == defect):
                print ("Element Exists")
                print(defect)
            else:
                print("Non Match")
 """