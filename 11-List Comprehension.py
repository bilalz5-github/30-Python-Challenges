def main():
    
   n = int(input("Enter the number of natural numbers you want the squares of: "))
   squares = [i * i for i in range(1, n + 1)]  # List comprehension
   print(squares)
   
if __name__ == "__main__":
   main()
