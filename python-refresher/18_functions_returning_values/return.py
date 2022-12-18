def add(x, y):
    print(x + y)
    return x +  y

result = add(5, 8)
print(result)
## 13
## 13

# 13 is first printed out from the function 'print(x + y)', then printed out again from the 'print(result)' statement

# 'return' statement ends any function after it returns the value
print("~~~~~~~~Return Function before Print~~~~~~~~")

def add(x, y):
    return x + y
    print(x + y)    # Since this is after the 'return', this print will never get called

result = add(5, 8)
print(result)
## 13