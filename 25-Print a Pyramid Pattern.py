def main():
    
    r = int(input("enter the number the of the rows; "))
    
    
   # c = int(input("enter the number the of the rows; "))
    
    
    for i in range(r):
        for j in range(r-i-1):
            print(" ", end="")
        for j in range(i+1) :
            print("*",end=" ")

        print("")
        
if __name__ == "__main__":
   main()