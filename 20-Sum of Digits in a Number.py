def main():
    intnum = int(input("Enter a number with two digits: "))
    total_sum = 0
    
    # Use intnum in the loop
    number = intnum  # Create a copy to preserve the original number for further use if needed
    
    while number > 0:
        total_sum += number%10  # Extract the last digit and add it to the sum
        number //= 10             # Remove the last digit
    
    print(f"The sum of the digits in {intnum} is {total_sum}")

if __name__ == "__main__":
    main()
