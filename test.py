# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.

def int_sum(dictionary):
    # if type(dictionary) is int:
    #     return dictionary

    # int_values = []
    sum_value = 0

    for x in dictionary.values():
        if type(x) is int:
            # int_values.append(x)
            sum_value += x

    # for i in int_values:
    #     sum_value + i

    return sum_value

new_dict = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

print(int_sum(new_dict))