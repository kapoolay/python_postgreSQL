# '*' collects all positional arguments
# '**' collects all keyword arguments
# Using both */** is normally used to accept an unlimited number of arguments
# so that some/all of those arguments can be passed into another function
## see example below

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)
# (1, 3, 5)    --> positional functions printed (*)
# {'name': 'Bob', 'age': 25}    --> keyword arguments printed (**)

# ~~~~~~~~~~~~~Example~~~~~~~~~~~~~
"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs
"""