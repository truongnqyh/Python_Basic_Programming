sentence = input("Enter a sentence: ")

# Split the sentence 
words = sentence.split()

# Initialize dictionary
word_cnt = {}

# Count word frequency
for word in words:
    word = word.lower()
    if word in word_cnt:
        word_cnt[word] += 1
    else:
        word_cnt[word] = 1

print(word_cnt)