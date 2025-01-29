def main():
    """"array for geeting data"""
    dataList=[]
    data = input("enter at least 5 numbers\n")
    
    number = data.split()
    
    for numbers in number:
     dataList.append(int(numbers) )
    
    print("stored data is: ", dataList)
    
    largestnumb = 0 
    
  #  largest_number = max(dataList)
   # print(largest_number)
    
    "now i am going to through each number and if the any given number is largests it will print """
    
    for n in dataList:
        if n > largestnumb:
            largestnumb=n
            
    
    
    print( "the largest number in the list is ", largestnumb)        
             
            
            
    
if __name__=="__main__":
     main()