# '**' collects keyword arguments into a dictionary

def named(**kwargs):    # 'kwargs' is just the parameter name we are using for 'keyword arguments'. This can be anything
    print(kwargs)

named(name="Bob", age=25)
## {'name': 'Bob', 'age': 25}

details = {"name": "Bob", "age": 25}
named(**details)
## {'name': 'Bob', 'age': 25}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Unpack a dictionary into named arguments using '**'

def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

# '**' assigns 'name' and 'age' as keys for the arguments and prints their value
named(details["name"], details["age"])
## Bob 25
### ^ is the same as below
named(**details)
## Bob 25

# # Using the dictionary name as a positional argument will return wrong result
# named(details, 25)
# ## {'name': 'Bob', 'age': 25} 25