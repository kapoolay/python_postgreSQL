# '*' allows a function to take in any number of arguments
# '*' collects all positional arguments

def multiply(*args):
    print(args)

multiply(1, 3, 5)
## (1, 3, 5)

print("Function using 'return'")

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total    # total = 1 * 3 * 5 = 15

print(multiply(1, 3, 5))
## (1, 3, 5) ----> it first prints out the inputted args because of "print(args)" from calling "multiply(1, 3, 5)"
## 15        ----> prints out the return 'total' because of "print(multiply(1, 3, 5))"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

