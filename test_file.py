#we define w as a list of words
w = ["haythem", "is", "eating", "tacos.", "haythem", "loves", "tacos", "", ":"]

#we define an empty dictionary that will hold the token/frequency key-value pair
#  key:word, value:int that corresponds to the frequency of occurrence
freq_occur = dict()

#your code goes here

for word in w:
    if word == freq_occur[word]:
        freq_occur[word] = 1
    # else:
    #     freq_occur[word] + 1

print(freq_occur)
