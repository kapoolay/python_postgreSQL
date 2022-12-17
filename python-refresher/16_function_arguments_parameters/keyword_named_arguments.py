## Recommendation is to use keyword arguments in more complicated functions for cleaner/clearer code

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(15, 0)
# You fool!

divide(dividend=15, divisor=0)
# You fool!

## not all arguments have to be keyword arguments
divide(15, divisor=3)
# 5.0

## Positional arguments have to go before the keyword arguments, otherwise you will get an error
divide(dividend=15, 3)
# SyntaxError: positional argument follows keyword argument