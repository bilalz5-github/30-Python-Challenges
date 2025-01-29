def main():
    text = input("enter the text to count:  ")
    
    count = 0
    
    for charcter in text:
        
        if (charcter in  "aAiIeEoOuU"):
            
            count += 1
            
    print(count)
     
     
if __name__ == "__main__":
    main()            
    
        
    
      