# List comprehension allows you to create lists on the fly with existing lists

numbers = [1, 3, 5]
doubled = []

# normal/traditional for loop
for x in numbers:
    doubled.append(x * 2)

print(doubled)

# List Comprehension Version
# the "for" loop is added into the variable

numbers = [1, 3, 5]
doubledV2 = [x * 2 for x in numbers]    # for every value in numbers, multiply by 2 and append it to the "doubledV2" list

print(f"{doubledV2} --> List comprehension version")




