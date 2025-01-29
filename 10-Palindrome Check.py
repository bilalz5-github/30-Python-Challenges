def main():
    data = input("whats your string : ")
    
    
    
    normalized_data = ''.join(char.lower() for char in data if char.isalnum())
    
    
    ReversedData = normalized_data[::-1]
    
    if normalized_data == ReversedData :
    
        print("yes string is plaindrome")
    else:
        
        print("no thats not plaindrome")
        
        

if __name__ == "__main__":
    main()
