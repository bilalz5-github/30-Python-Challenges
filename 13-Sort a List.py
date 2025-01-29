def main():
    user_list = input("Enter the data of number from")
    
    split_list = list(map(int, user_list.split()))
    split_list.sort()
    
    print(split_list)
    
   
if __name__ == "__main__":
   main()
