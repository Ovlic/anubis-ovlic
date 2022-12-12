def title_case(a_string):
    """
    Change to title case where stopwords like "and" aren't capitalized.
    
    Parameters:
    a_string (str): input string with any mix of upper and lower case
    
    Return value:
    str: output string with capitalization like a book title
    """
    
    stop_words = ['and', 'the', 'a', 'in', 'are', 'is', 'to', 'with', 'of']
    new_title = ""
    start = False # Variable to check if loop is at the first word
    
    for word in a_string.split(" "):
        
        if start == False: # start is false
            print(f"Word: '{word}'; First word in text, capitalizing to '{word.capitalize()}'")
            new_title += word.capitalize() # Capitalze the word
            start = True # Set start to true so this statement can't run again
            continue # Continue to the next word

        new_title += " " # Add a space

        if word.lower() in stop_words: # If word is a stop word
            print(f"Word: '{word}'; Found in stop_words, lowerizing to '{word.lower()}'")
            new_title += word.lower() # Lowercase the word

        else: # If the word is not a stop word
            print(f"Word: '{word}'; Not found in stop_words, capitalizing to '{word.capitalize()}'")
            new_title += word.capitalize() # Capitalize the word

    return new_title


def main():
    e = title_case("hi")
    print(e)


if __name__ == "__main__":
    main()
