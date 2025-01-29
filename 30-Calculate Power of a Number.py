def main():
       # Recursive function defined within main to calculate the power of a number
    def power(base, exponent):
        if exponent == 0:
            return 1
        else:
            return base * power(base, exponent - 1)
    
    # Get input from the user
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))

    # Calculate the power and display the result
    result = power(base, exponent)
    print(f"The result of {base} raised to the power of {exponent} is {result}")
if __name__ == "__main__":
    main()
