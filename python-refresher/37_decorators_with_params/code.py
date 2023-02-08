import functools

user = {"username": "kevin", "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)      ## allows 'secure_function' to keep the original function's name/documentation globally
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} admin permissions for {user['username']}."

        return secure_function

    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


user = {"username": "kevin", "access_level": "guest"}
print(get_admin_password())
print(get_dashboard_password())
'''
No admin admin permissions for kevin.
No user admin permissions for kevin.
'''

user = {"username": "anna", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())
'''
admin: 1234
No user admin permissions for anna.
'''
