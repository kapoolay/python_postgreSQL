# Function that prints a dictionary into a nice format

def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)    # calling 'named' function to print arguments out
    for arg, value in kwargs.items():    # this will iterate thru the dictionary, grabbing arg and value from each item
        print(f"{arg}: {value}")         # and print it nicely

print_nicely(name="Bob", age=25)
## {'name': 'Bob', 'age': 25}
## name: Bob
## age: 25