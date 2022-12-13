# use "*" operator to collect leftover values when performing a destructuring assignment

head, *tail = [1, 2, 3, 4, 5,]
print(head)
print(tail)

# grab the first and last items, then gather up the middle
head, *middle, tail = [1, 2, 3, 4, 5,]
print(head)
print(middle)
print(tail)

# grab the first three items, and bundle up the rest
first, second, third, *rest = [1, 2, 3, 4, 5,]
print(first, second, third, rest)