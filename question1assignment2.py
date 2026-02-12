# question 1

file = open(file="sample-file.txt", mode="r")

dictionary_of_words = {}
list_of_words = []
for word in file.read().split(): # gets all the individual words
    word = word.lower() # lowercase the whole word
    word = word.strip(",.") # removes any commas or periods from the word

    word_length = len(word)
    if word_length >= 2:
        list_of_words.append(word) # to keep track of each word

for each_word in list_of_words: # for every word in our entire list of words
    # adds each word to the dictionary as a key, and set the value as 0 for now
    dictionary_of_words[each_word] = 0

for word_appearance in list_of_words:  # updates how many times each word appears
    dictionary_of_words[word_appearance] += 1

sorted_dictionary_of_words=dict(sorted(dictionary_of_words.items(), key=lambda item: item[1], reverse=True))
print(sorted_dictionary_of_words)

list_of_sorted_words = []

for word in sorted_dictionary_of_words:
    list_of_sorted_words.append(word)

print(list_of_sorted_words)

for i in range(0, 10):
    most_occurring_word = list_of_sorted_words[i]
    print(f"{list_of_sorted_words[i]} -> {sorted_dictionary_of_words[most_occurring_word]}")

file.close()
