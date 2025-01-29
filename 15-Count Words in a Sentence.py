def CWS():
    sentence = input("Count the Words in Sentence")
    words = sentence.split()
    
    counter = 0 
    
    for  i in words: 
        
        counter += 1 
   
    print(counter)
if __name__ =="__main__":
    CWS()
