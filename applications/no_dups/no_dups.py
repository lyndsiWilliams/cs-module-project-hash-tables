def no_dups(s):
    # Your code here

    # Create the cache for storage
    cache = {}

    # Split the parameter string into a list of words
    # and store this list to a variable (words)
    words = s.split()

    # Loop through the length of the words list
    for i in range(len(words)):
        # If the current iteration does not exist in the cache
        if words[i] not in cache:
            # Put that word in the cache
            cache[words[i]] = 0

    # " ".join() = put the words back together
    # keys() = ensure that the words are in the order that they were entered
    # strip() = remove any extra white space
    duplicates_removed = " ".join(cache.keys()).strip()

    return duplicates_removed




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))