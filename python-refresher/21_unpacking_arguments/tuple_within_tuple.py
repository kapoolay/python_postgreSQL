def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total

def apply(*args, operator):     # collect all of the positional arguments into tuple '*args', and also have a named argument at the end
    if operator == "*":
        return multiply(*args)    # since the multiply function above uses '(*args)', you need to use the '*' or else it will return the tuple itself
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="*"))    # YOU MUST pass in the named argument "operator"
## 17

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUGGING the multiply function
print("~~~~~~~~~~~~~~~BUGGED~~~~~~~~~~~~~~~")

def multiply(*args):    # '*args' creates a tuple of the individual arguments
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(args)    # BUG -> we are not passing the individual arguments, instead we're passing the 'args' tuple created from the "multiply(*args):" function
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="*"))
# the 'print(args)' from the 'multiply' function prints a tuple of tuples. Then when you iterate "for arg in args:", 'arg' is the inner tuple
## ((1, 3, 6, 7),)
# you're then multiplying that tuple * 1, which returns the tuple as the 'total'
## (1, 3, 6, 7)