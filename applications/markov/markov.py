import random
import string

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# Split the words string into a list of separate words and store it in a variable
split_words = words.split()

# Check for uppercase letters using string library
upper_check = [i for i in string.ascii_uppercase]
# Check for "stop word" characters
end_check = ['!', '.', '?']

# Create a dictionary for the approved "follow words"
follow_words = {}

# Loop through the length of the split_words list
# to create a referenceable key for each word and
# store the words in the follow_words dictionary
for i in range(len(split_words)):
    # If the current iteration + 1 is less than the length of the list (empty list check)
    if i + 1 < len(split_words):
        # If the current iteration is already in the dictionary
        if split_words[i] in follow_words:
            # This is a duplicate word
            # Append the iteration with a +1 to the key (to allow dupes)
            follow_words[split_words[i]].append(split_words[i + 1])
        # Otherwise, the iteration does not exist in the dictionary
        else:
            # Add this iteration to the dictionary for the very first time
            follow_words[split_words[i]] = [split_words[i + 1]]
    # Otherwise, the list is empty
    # else:
    #     follow_words[split_words[i]] = []

# A function that will determine and choose a random start word
def start_word():
    # Makes a random list from the list of approved follow words by their keys
    key = random.choice(list(follow_words.keys()))

    # Go through the random list and check if:
        # The first character is upper case OR
        # The first character is " AND the second character is upper case
    if key[0] in upper_check or key[0] == '"' and key[1] in upper_check:
        return key
    # If not, run the function again to find a start word (recursion!)
    else:
        return start_word()

# A function that will determine if a word is a stop word and return a boolean
def stop_word(word):
    # If the last character is in the end check OR
    # If the last character is " and the second-to-last character is in the end check
    if word[-1] in end_check or word[-1] == '"' and word[-2] in end_check:
        return True
    else:
        return False

# A function that will create a new sentence
def create_sentence(word):
    # If the word is NOT a stop word:
    if not stop_word(word):
        # Choose a random follow word
        random_word = random.choice(follow_words[word])

        # Create a list of random words then
        # Recursively run the function
        # It will run until it hits a stop word
        return [word] + create_sentence(random_word)
    
    # Return the new sentence
    return [word]


# TODO: construct 5 random sentences
# Your code here

# Run the function 5 times to create 5 sentences
for i in range(5):
    # Create a new start word
    new_start = start_word()

    # Join the randomly-generated words together
    # With spaces inbetween each word
    # Starting with new_start
    # end = " " makes it so that all sentences for one paragraph
    # Avoiding the default of a new sentence for each line
    print(" ".join(create_sentence(new_start)), end = " ")