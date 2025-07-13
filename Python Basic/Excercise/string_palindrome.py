## What is palindrome string?
# same forward and backward
# Ex: "madam" "racecar" "level" "121"
# Or "A man a plan a canal Panama" (if we ignore spaces and cases)

# Convert string ---> text[start:stop:step]
import re

# char.isalnum() ~ filter only LETTERS and NUMBERS ~ alphanumeric (a-z, A-Z, 0-9)
def is_palindrome(text):
    # # Step 1: Make all characters lowercase
    # text = text.lower()

    # # Step 2: Keep only letters and numbers
    # cleaned_text = ""
    # for char in text:
    #     if char.isalnum():  # isalnum() = is alphanumeric (a-z, A-Z, 0-9)
    #         cleaned_text += char

    # # Step 3: Reverse the cleaned text
    # reversed_text = cleaned_text[::-1]
    text = "".join(char.lower() for char in text if char.isalnum())

    # Step 4: Check if the original cleaned text is the same as the reversed one
    return text == text[::-1]

input_text = input("Enter a sentence: ")

if is_palindrome(input_text):
    print(f"{input_text} is a palindrome string")
else:
    print(f"{input_text} is NOT a palindrome string") 
