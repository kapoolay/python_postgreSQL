def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

# List comprehension
doubled_list_comprehension = [double(x) for x in sequence]    # list comprehension
print(f"List Comprehension: {doubled_list_comprehension}")

# Using Map with a lambda function
doubled_map = list(map(lambda x: x * 2, sequence))    # to print a map out, you need to turn it into a list
print(f"Map: {doubled_map}")


# Printing out a map without turning it into a list(), prints out the following
map_object = map(lambda x: x * 2, sequence)
print(map_object)
## <map object at 0x10f152fa0>