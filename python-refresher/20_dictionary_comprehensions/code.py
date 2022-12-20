# Much like a list comprehension, but will get a dictionary at the end. Will need to assign key:value pairs, rather than just values

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

# for every name in the dictionary, print out their information --> Name: (value1, value2, value3)
username_mapping = {user[1]: user for user in users}

print(username_mapping)
## {'Bob': (0, 'Bob', 'password'), 'Rolf': (1, 'Rolf', 'bob123'), 'Jose': (2, 'Jose', 'longp4assword'), 'username': (3, 'username', '1234')}

#~~~~~~~~~~Pull Bob's information out~~~~~~~~~~
print(username_mapping["Bob"])
## (0, 'Bob', 'password')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# If you didn't have a "username_mapping", you would have to write out the whole 'for' loop

for user in users:
    if user[1] == "Bob":
        print(user)
    else:
        print(f"not Bob - this is {user[1]}.")

# (0, 'Bob', 'password')
# not Bob - this is Rolf.
# not Bob - this is Jose.
# not Bob - this is username.