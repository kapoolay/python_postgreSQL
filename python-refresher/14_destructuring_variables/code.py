# normal tuple, brackets are not necessary unless the tuple is placed in a list[]
x = (5, 11)
# can also be written as
x = 5, 11

# 5 and 11 can also be put into 2 variables
x, y = (5, 11)
print(x, y)

# python is smart enough to assign each value in the tuple to different variables
t = 3, 4, 5
a, b, c = t
print(a, b, c)