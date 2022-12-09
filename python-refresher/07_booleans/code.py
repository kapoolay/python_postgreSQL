# Booleans are values either True or False
# Comparisons: ==, !=, >, <, >=, <=

#print(5 == 5)
#print(5 > 5)
#print(10 != 10)    # is 10 different from 10

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Python Boolean Key Words (RECOMMENDED TO NEVER USE 'is')
# 'is' used to compare whether two elements are exactly the same

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
abroad2 = friends

print(friends == abroad)
print(friends is abroad)  # list 'friends' is saved in a different memory from list 'abroad'. Python doesn't see these as the same.
print(friends is friends) # saved in the same memory, Python sees it to be the same
print(friends is abroad2) # 'abroad2' variable points to the 'friends' list, not a new list