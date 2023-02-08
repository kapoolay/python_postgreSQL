import functools

user = {"username": "kevin", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)      ## allows 'secure_function' to keep the original function's name/documentation globally
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

## rather than doing this, you can use '@'.
# get_admin_password = make_secure(get_admin_password)

@make_secure        # doing this replaces the 'get_admin_password' function name to be 'secure_function" from the 'make_secure' function
def get_admin_password():
    return "1234"

print(get_admin_password.__name__)      # get_admin_password

print(get_admin_password())             # No admin permissions for kevin.

'''
Not using the imported '@functools.wraps(func)' will result in the name to be changed from the original function name to the one taking it over:

get_admin_password --> secure_function
'''
