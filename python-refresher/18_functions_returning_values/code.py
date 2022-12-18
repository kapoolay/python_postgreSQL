# Functions return "None" by default

def add(x, y):
    print(x + y)    # this prints the value of the function, but returns "None"

add(5, 8)
## 13

result = add(5, 8)
## 13
print(result)
## None

# You can assign the return value of a function by using the "return" keyword INSTEAD of "print"
print("~~~~~~~~~~Return Function Result~~~~~~~~~~")

def add(x, y):
    return x + y    # this returns the value of the function, but doesn't print anything out

add(5, 8)    # This line does not print anything since we are using "return"
result = add(5, 8)    # 'result' now equals the return value of the function, "5 + 8" in this case
print(result)
## 13

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Common mistakes made
print("~~~~~~~~~~Common Mistakes~~~~~~~~~~")

def add(x, y):
    print(x + y)

# This first calls the function and prints '13'
# Then returns 'None' because functions by default return none
print(add(5, 8))
## 13
## None