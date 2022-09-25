# Arham Zubair - 22 September 2022

# Pseudocode
# 1. Convert a string to lowercase characters.
# 2. Split the lowercase string into individual words.
# 3. Count the number of words in the lowercase string.
# 4. Determine the number of distinct words in the lowercase string.
# 5. Calculate the number of times each word appears in the lowercase string.
# 6. Remove the punctuation from the lowercase string.
# 7. Perform a count analysis on the text without punctuation characters.

# Importing the string module, which includes the punctuations too
# Creating a punctuation list only
import string
punctuation = string.punctuation

default_para = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""

# Removing case-sensitivity by converting all to lowercase
s_lower = default_para.lower()

# Assigning an empty list() to the words variable changes the variable type to a list (an array in python).
words_list = list()

# Splitting the words
words_list = s_lower.split()

word_list_length = len(words_list)
print(f"The length of the splitted word list is: {word_list_length}")

# converting the words list into a set.
# Set items are unordered, unchangeable, and do not allow duplicate values.
words_set = set(words_list)
words_set_length = len(words_set)
print(f"After the conversion from list to set, the length of the set is: {words_set_length}")

# creating an empty dictionary
word_freq = dict()

# for each word in the list, check if the word is already in the dictionary
for word in words_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


print(word_freq)
