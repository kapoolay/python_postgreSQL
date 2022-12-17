## This is not recommended
## Always try to stick the default value in the function --> def add(x, y=3):
default_y = 3

def add(x, y=default_y):
    print(x + y)

add(2)
# 5

## Redefining a variable's value after it's been called as a
## default parameter value will not modify the value
default_y = 4
add(2)
# 5

