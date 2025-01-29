def main():
    datalist = []
    numbers = input("Enter the numbers so I can check it for you: ")
    number_strings = numbers.split()
    
    # Convert string inputs to integers
    for number_string in number_strings:
        datalist.append(int(number_string))
        
    print("The given numbers are ", datalist)
    
    # Check and print prime numbers from the list
    for n in datalist:
        if is_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")

def is_prime(num):
    """Check if the number is prime."""
    if num <= 1:
        return False  # 1 or less are not prime numbers
    for i in range(2, int(num**0.5) + 1):  # Check for factors from 2 to sqrt(num)
        if num % i == 0:
            return False  # Found a factor, so num is not prime
    return True  # No factors found, num is prime

if __name__ == "__main__":
    main()
