def main():
    
    string1 = input("enter the first word ")
    string2 = input("enter the second word ")
    
    string1 = string1.lower()
    string2 = string2.lower()
    
    
    on1 = len( string1)
    tw2 = len(string2)
    
    print( on1 , tw2 )
    
    for char in string1:
        if char in string2:
            # Remove the first occurrence of char from string2
            string2 = string2.replace(char, '', 1)
        else:
            print("No, they are not anagrams.")
            break
    else:
        # If the loop completes without breaking, check if string2 is empty
        if not string2:
            print("Yes, they are anagrams!")
        else:
            print("No, they are not anagrams.")

if __name__ == "__main__":
       main() 