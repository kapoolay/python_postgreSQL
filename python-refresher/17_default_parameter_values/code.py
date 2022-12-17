def add(x, y=8):
    print(x + y)

add(5)
# 13

add(x=5)    #keyword
# 13

add(x=5, y=10)
# 15


## 'x' is a required argument, and will produce an error if not provided
add(y=5)
# TypeError: add() missing 1 required positional argument: 'x'