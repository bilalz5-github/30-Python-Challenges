def main():
    user_data = input("Enter multiple values separated by spaces:").split()
    print(user_data)
    noe=0
    addd=0
    for i in user_data:
       noe += 1
       
       addd += int(i)

    print(noe)
    
    result = addd/noe
    
    print(result)
         
   
if __name__ == "__main__":
   main()
