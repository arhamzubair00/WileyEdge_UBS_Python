# Arham Zubair


# Convert the string to lowercase characters.
# Split the lowercase string into individual words.
# Remove the punctuation from the lowercase words. Assume that all punctuation is either the first character or the last character of each item in the list.
# Perform a count analysis on the words without punctuation characters.
# Display the dictionary with the word counts and the number of distinct words in the original string.

import string

punctuation = string.punctuation

default_para = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""

s_lower = default_para.lower()

words_list = list()

words_list = s_lower.split()

w_clean = list()

for w in words_list:
    if w in punctuation or w == "":
        continue
    elif len(w) == 1:
        w_clean.append(w)
    elif w[-1] in punctuation and w[0] not in punctuation:
        sliced_word = w[0:-1]
        if sliced_word[-1] in punctuation:
            sliced_word2 = sliced_word[0:-1]
            w_clean.append(sliced_word2)
        else:
            w_clean.append(sliced_word)
    elif w[0] in punctuation and w[-1] not in punctuation:
        sliced_word = w[1:]
        w_clean.append(sliced_word)
    else:
        w_clean.append(w)


word_freq = dict()

for word in w_clean:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)
