def main():
    str1 = input("Enter the string  that you want to remove the space: ")
    
    #str2 = str1.replace(" ","")
    
   # print(str2)
    
    str3 = ""
    
    for  i in str1:
         if i != " ":
             str3 = str3 + " "
             print(str3)
    
    
if __name__ == "__main__":
   main()