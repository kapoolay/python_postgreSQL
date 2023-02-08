user = {"username": "kevin", "access_level": "guest"}

def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            print(f"No admin permissions for {user['username']}.")

    return secure_function

## We are replacing the original 'get_admin_password' function with the 'make_secure'
get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
'''
No admin permissions for kevin.
None
'''