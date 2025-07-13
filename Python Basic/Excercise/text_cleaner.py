import re

#### re.sub(pattern, repl, text)

# r"..." ~ raw string
def text_cleaner(text):
    # Remove punctuation 
    #  \w ~ [a-zA-Z0-9_]
    #  \s ~ (space, tab, newline, v.v.)
    #  ^ ~ negation ~ ><
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    return text.lower()

input_text = input("Enter a sentence: ")
cleaned_text = text_cleaner(input_text)
print(f"From: {input_text} ---->>> {cleaned_text}")