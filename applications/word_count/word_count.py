def word_count(s):
    # Your code here

    # Create the cache for storage
    cache = {}

    # Set the invalid characters to a variable
    invalid = '":;,.-+=/\\|[]{}()*^&'

    # Set a variable for the string
    # once the invalid characters are removed
    corrected_string = ""

    # Loop through the characters in the parameter string
    for i in s:
        # If the character isn't an invalid character
        if i not in invalid:
            # Add it to the corrected string
            corrected_string += i

    # strip() - remove all white space
    # lower() - make all characters lowercase
    # split() - split the corrected parameter string into a list of words
    # and store this list to a variable (words)
    words = corrected_string.strip().lower().split()

    # Loop through the length of the words list
    for i in range(len(words)):
        # If the current iteration does not exist in the cache
        if words[i] not in cache:
            # Create an empty space in the cache for it
            # This starts the word count for that word
            cache[words[i]] = 0

        # Otherwise, it exists in the cache so increase the word count by 1
        cache[words[i]] += 1

    # Return the cache, which will hold the current word count
    return cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))