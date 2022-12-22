def myfunction(**kwargs):
    print(kwargs)

myfunction(**"Bob")    # Error, must be mapping. "Bob" is not a dictionary.
myfunction(**None)    # Error -> 'None' is not a dictionary

# If you're working with variables in your code and
# you are passing them unpacked to a function,
# then you must make sure they are dictionaries.
# If they are anything else, you will get an error.

