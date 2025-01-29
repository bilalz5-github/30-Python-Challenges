from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def calculator():
    print("Simple Calculator 🧮")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)} ✨")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)} ✨")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)} ✨")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)} ✨")
    else:
        print("Invalid input! Please choose a valid operation. ⚠️")

# Run the calculator
if __name__ == "__main__":
    calculator()
