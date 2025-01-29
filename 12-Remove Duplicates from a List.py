def main():
    user_list = input("Enter the data of number from")
    
    split_list = user_list.split()
    
    my_list =  set(split_list)

    print(my_list)
   
if __name__ == "__main__":
   main()
