#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

# Word frequency exercise

import re

# This is a function that checks if a text qualifies as a sentence.
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w', text):
        return False

    return True


# Prompt the user for input
user_sentence = input("Enter a sentence: ")

# Keep asking until a valid sentence is entered
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Step 2: Split into words (make lowercase, strip punctuation)
words = re.findall(r'\b\w+\b', user_sentence.lower())

# Step 3: Create lists
unique_words = []
frequencies = []

# Step 4: Iterate and update frequencies
for word in words:
    if word in unique_words:
        index = unique_words.index(word)
        frequencies[index] += 1
    else:
        unique_words.append(word)
        frequencies.append(1)

# Step 5: Print results
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")

