def main():
    
    num =input("enter number as many as you want my putting the spcae: ").split()
    
    num_list = []  # Create an empty list to store the integers
    for i in num:
        num_list.append(int(i))  # Convert each string to an integer and append it to num_list
    print(num_list)

    maxnumber = num_list[0]
    minnumber = num_list[0]
    
    # Loop through the list to find max and min
    for number in num_list:
        if number > maxnumber:
            maxnumber = number
        if number < minnumber:
            minnumber = number
    
    # Print the results
    print("Maximum number:", maxnumber)
    print("Minimum number:", minnumber)
    

if __name__ == "__main__":
    main()
