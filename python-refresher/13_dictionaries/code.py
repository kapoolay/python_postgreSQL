# Associates keys:values

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

# you must access the keys to pull out information
adam_age = friend_ages["Adam"]
print(f"Adam is {adam_age} years old")

# Adding a key/pair to the dictionary
friend_ages["Bob"] = 20
print(friend_ages)

# changing an existing value
friend_ages["Bob"] = 50
print(friend_ages)