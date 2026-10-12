# Word Counter

# take a text from user
text = input("write your text: ")

# broke the to words
words = text.split()

# count the words
total_words = len(words)

# count the characters
total_characters = len(text)


# result
print("total words:", total_words)
print("total characters:", total_characters)
