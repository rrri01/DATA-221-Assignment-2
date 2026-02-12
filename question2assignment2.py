# question 2

file = open(file="sample-file.txt", mode="r")

dictionary_of_words = {}
list_of_words = []
for word in file.read().split(): # gets all the individual words
    word = word.lower() # lowercase each token
    word = word.strip(",.")  # removes any commas or periods from the word

    word_length = len(word)
    if word_length >= 2:
        list_of_words.append(word) # to keep track of each word

list_of_bigrams = []

for i in range(0, (len(list_of_words)-1)):
    bigram_to_append = f"{list_of_words[i]} {list_of_words[i+1]}"
    list_of_bigrams.append(bigram_to_append)

dictionary_of_bigrams = {}

for each_bigram in list_of_bigrams: # for every bigram in our entire list of bigrams
    # adds each bigram to the dictionary as a key, and set the value as 0 for now
    dictionary_of_bigrams[each_bigram] = 0

for bigram_appearance in list_of_bigrams:  # updates how many times each bigram appears
    dictionary_of_bigrams[bigram_appearance] += 1

sorted_dictionary_of_bigrams=dict(sorted(dictionary_of_bigrams.items(), key=lambda item: item[1], reverse=True))
list_of_sorted_bigrams = []

for bigram in sorted_dictionary_of_bigrams:
    list_of_sorted_bigrams.append(bigram)

for i in range(0,5):
    most_occurring_bigram = list_of_sorted_bigrams[i]
    print(f"{list_of_sorted_bigrams[i]} -> {sorted_dictionary_of_bigrams[most_occurring_bigram]}")

file.close()
