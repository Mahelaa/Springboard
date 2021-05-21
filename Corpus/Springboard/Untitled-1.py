
   """  #Get indivisual word
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