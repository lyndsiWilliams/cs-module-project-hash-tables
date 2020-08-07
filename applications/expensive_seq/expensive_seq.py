# Your code here

# Create the cache for storage
cache = {}


def expensive_seq(x, y, z):
    # Your code here

    # Set a base case
    if x <= 0:
        return y + z

    # Check if the calculated value exists in the cache
    if (x, y, z) in cache:
        return cache[(x, y, z)]

    # Otherwise, the value needs to be calculated and stored
    else:
        cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    # Return the cached value
    return cache[(x, y, z)]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
