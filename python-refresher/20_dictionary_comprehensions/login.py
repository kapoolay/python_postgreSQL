users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ the 'username_mapping' dictionary comprehension saves you from adding the following for
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ loop to check if they're inputting the right username for their input

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")

## Enter your username: Bob
## Enter your password: password
## Your details are correct!

## Enter your username: kevin
## Enter your password: password
## Traceback (most recent call last):
##   File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/20_dictionary_comprehensions/login.py", line 13, in <module>
#     _, username, password = username_mapping[username_input]
# #KeyError: 'kevin'