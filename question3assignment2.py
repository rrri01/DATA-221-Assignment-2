
file = open(file="sample-file.txt", mode="r")

unfiltered_lines = []
all_the_lines = []
for line in file:
    unfiltered_lines.append(line)
    line = line.lower()  # lowercase each token

    for character in line: # this loop replaces every space, comma, or period with nothing, aka it removes it.
        if character==" ":
            line = line.replace(character, "")
        if character==",":
            line = line.replace(character, "")
        if character==".":
            line = line.replace(character, "")
        if character=="-":
            line = line.replace(character, "")
        if character =="\n":
            line = line.replace(character,"")

    all_the_lines.append(line)
dictionary_of_near_duplicates = {}

for each_line in all_the_lines: # for every line in our entire list of lines
    # adds each line to the dictionary as a key, and set the value as 0 for now
    dictionary_of_near_duplicates[each_line] = 0

for line_appearance in all_the_lines:  # updates how many times each bigram appears
    dictionary_of_near_duplicates[line_appearance] += 1

dictionary_of_near_duplicates.pop("")
sorted_dictionary_of_near_duplicates=dict(sorted(dictionary_of_near_duplicates.items(), key=lambda item: item[1], reverse=True))

list_of_sorted_near_duplicates = []

for line in sorted_dictionary_of_near_duplicates:
    list_of_sorted_near_duplicates.append(line)

# print(sorted_dictionary_of_near_duplicates)
# print(list_of_sorted_near_duplicates)

for i in sorted_dictionary_of_near_duplicates:
    if sorted_dictionary_of_near_duplicates[i]>= 2:
        print(f"{all_the_lines.index(i)+1}")
        # add 1 to the index before printing because list index starts at 0, but normally when we are counting lines of a text, we start at 1 instead of 0
        print(i)

file.close()
