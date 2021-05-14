# Your code here
import string

def histo(file_name):
    # Open and read the parameter file
        with open(file_name, "r") as f:
            file = f.read()

    # Split the parameter file into a list of separate words
    words = file.split()

    # Set a variable for the longest word to use to justify left
    longest_word = ""

    # Loop through the length of the words list
    for i in range(len(words)):
        # Set a variable for the corrected word
        corrected_word = ""

        # Loop through the current iteration of a word
        for j in words[i]:
            # Check if the current word is alphanumaric (letters/nums)
            if j.isalnum():
                # If so, add the word as a corrected word
                corrected_word += j

        # Set the current word to it's corrected word and make it lower case
        words[i] = corrected_word.lower()

        # This will make the words go in order from longest to shortest
        if len(words[i]) > len(len(longest_word)):
            longest_word = words[i]

    # Set a dictionary to store the word count
    word_count = {}

    # Loop through the list of words
    for i in words:
        # If the current iteration already exists in the word count
        if i in word_count:
            # Add another # to the tally for this word
            word_count[i] += "#"
        # Otherwise, this is the first occurrence so start the tally for this word
        else:
            word_count[i] = "#"

    # Sort the words by their number of #s
    count_sort = {key: value for key, value in sorted(word_count.items(), key=lambda item: len(item[1], reverse=True))}

    # Sort alphabetically
    alpha_sort = {key: value for key, value in sorted(word_count.items(), key=lambda key:key)}

    # Print the words sorted by count
    for key in count_sort:
        print(f"""{key.ljust()})
