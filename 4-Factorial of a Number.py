def main():
    
    number = int(input("for what number of factorial you need"))
    z=1
       # Calculate factorial using a while loop
    n = number
    while n > 1:  # Continue while n is greater than 1
        z *= n    # Multiply z by n
        n -= 1    # Decrement n by 1
    
    # Print the result
    print(f"The factorial of {number} is {z}")
if __name__=="__main__":
        main()