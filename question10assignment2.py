# question 10

def find_lines_containing(filename, keyword):
    list_of_words_per_line = []
    keyword = keyword.lower()
    list_of_lines = [] # unfiltered lines

    file = open(filename, mode="r")
    for line in file:
        line = line.strip("\n")

        list_of_lines.append(line)

        words_in_line = []
        for word in line.split():
            word = word.lower()

            for character in word:
                if character == "\n":
                    word = word.replace(character, "")
                if character == " ":
                    word = word.replace(character, "")
                if character == ",":
                    word = word.replace(character, "")
                if character == ".":
                    word = word.replace(character, "")
                if character == "-":
                    word = word.replace(character, "")

            words_in_line.append(word)
        # print(words_in_line)
        list_of_words_per_line.append(words_in_line)
    # print(list_of_words_per_line)

    indexes_with_keyword = []

    for line in list_of_words_per_line: # for each line
        for word in line: # for each word the current line
            if keyword == word:
                line_index = list_of_words_per_line.index(line)
                indexes_with_keyword.append(line_index)
                break
    # print("x")
    # print(indexes_with_keyword)
    lines_with_word = []
    for i in indexes_with_keyword:
        # print(i)
        # print(list_of_lines[i])
        lines_with_word.append(list_of_lines[i])

    matching_lines_found = len(indexes_with_keyword)

    return matching_lines_found, lines_with_word[0:3]

# call the function
# there is no word "lorem" in the sample file
amount_of_lines, lines_with_keyword = find_lines_containing("sample-file.txt", "data")
print(f"matching lines: {amount_of_lines}")
print("first 3 matching lines:")

for i in lines_with_keyword:
    print(i)