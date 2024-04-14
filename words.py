import nltk
from nltk.corpus import words
import json
import random

# Download NLTK words corpus
nltk.download('words')

# Get the list of 5-letter words from NLTK
word_list = [word.lower() for word in words.words() if len(word) == 5]

# Choose a random word from the word list
WORD = random.choice(word_list)

# Save the word list to a JSON file
with open("words_list.json", "w") as f:
    json.dump({"words": word_list}, f)

# Rest of your code...
