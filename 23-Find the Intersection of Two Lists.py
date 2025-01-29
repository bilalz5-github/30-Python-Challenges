def main():
   first= [1,2,3,4,5,6,7,8,8]
   second=[2,2,3,34,3,23,25,345,24]
   
   third = list(set(first).intersection(set(second)))    
   print(third)    
if __name__ == "__main__":
    main()
