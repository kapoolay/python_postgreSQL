# '*' can be used to destructure arguments into multiple parameters

def add(x, y):
    return x + y  # to print the return, you need to add 'print' when calling the function

nums = [3, 5]
print(add(*nums))
## 8

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# '*' can also be used for destructuring dictionaries
def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))
## 40


# INSTEAD OF DOING THE ABOVE, you can tell python to pass in the 'nums' dictionary as named arguments
# where the argument will be equal to the value associated with that same name for a key
# '**' means you have a dictionary with 2 or more keys, I'm going to pass in each key as a
# named argument and the value is going to be that value associated with the key
def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}

print(add(**nums))
## 40

# ~~~~~~~~~~~~~~ Another example
def add2(a, b, c, d):
    return a + b + c + d

nums2 = {"a": 5, "b": 10, "c": 15, "d": 1}

print(add2(**nums2))
## 31