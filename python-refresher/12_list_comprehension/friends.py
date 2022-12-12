friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

# Traditional for loop
for friend in friends:
    if friend.startswith("S"):
            starts_s.append(friend)

print(starts_s)

# List Comprehension Version
friends2 = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen", "Steve"]
starts_s2 = [friend for friend in friends2 if friend.startswith("S")]

print(starts_s2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Lists are not exactly the same!!
# Lists with different names are never the same, even if contents are the same. Lists are saved in different places in memory
list1 = ["a", "b", "c"]
list2 = ["a", "b", "c"]
print("list1: ", id(list1), "list2: ", id(list2), "--> different locations in memory")

## However, if you use "=" for a list, it will be identical
list3 = ["a", "b", "c"]
list4 = list3
print("list3: ", id(list3), "list4: ", id(list4), "--> Same locations in memory")