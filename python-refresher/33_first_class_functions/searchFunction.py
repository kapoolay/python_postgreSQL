def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Anne Pun", get_friend_name))     # {'name': 'Anne Pun', 'age': 27}

print(search(friends, "Kevin C", get_friend_name))
'''
Traceback (most recent call last):
  File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/33_first_class_functions/searchFunction.py", line 18, in <module>
    print(search(friends, "Kevin C", get_friend_name))
  File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/33_first_class_functions/searchFunction.py", line 5, in search
    raise RuntimeError(f"Could not find an element with {expected}")
RuntimeError: Could not find an element with Kevin C
'''