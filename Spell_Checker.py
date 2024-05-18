import string
from enchant.checker import SpellChecker

def has_non_english_words(text_file):
  d = SpellChecker("en_US")
  non_english_words = set()
  with open(text_file, 'r') as file:
    for line in file:
      for word in line.split():
        word = word.strip(string.punctuation).lower()
        if not d.check(word):
          non_english_words.add(word)
  return non_english_words

# Example usage
text_file = "C:\\Users\\welcom\\Documents\\Coding\\Python\\vaani task\\Transcripts\\GMT20200214-102959_Nitin_Delo_1686x728_transcript.txt"
non_english_words = has_non_english_words(text_file)

if non_english_words:
  print("The file contains potential non-English words:", non_english_words)
else:
  print("The file seems to contain mostly English words.")