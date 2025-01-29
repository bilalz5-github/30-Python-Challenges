def concatenate_strings(string_list):
    # Joins the list of strings into a single string with spaces
    return ' '.join(string_list)

def main():
    # Prompt the user to enter a series of words
    data = input("Enter words separated by spaces: ")
    
    # Split the input string into a list of words
    words_list = data.split()
    
    # Call the concatenate_strings function to combine the list into one string with spaces
    result = concatenate_strings(words_list)
    
    # Print the result
    print("Concatenated String:", result)

if __name__ == "__main__":
    main()
