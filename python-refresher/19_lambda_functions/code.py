# Lambda Functions -> no function names, only used to return values
# Operate on inputs and return outputs, almost never used to perform actions
# Almost all single line, due to readability
# Recommendation is to define a normal function, rather than a lambda function

# ~~~~~ Normal Function
def add(x, y):
    return x + y

print(add(5, 7))
## 12

# ~~~~~ Lambda Function using the 'lambda' keyword
print((lambda x, y: x + y)(5, 7))
## 12

# #you can assign it to a variable
# add = lambda x, y: x + y
