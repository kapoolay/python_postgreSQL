import functools

user = {"username": "kevin", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)      ## allows 'secure_function' to keep the original function's name/documentation globally
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

@make_secure
def get_password(panel, arg2):        ## this takes requires a paramater. The decorator function that takes this over ALSO needs to be able to take params
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"
    else:
        return f"{arg2} is not an acceptable parameter."

print(get_password("billing", "test"))      # super_secure_password
print(get_password("admin", "test"))        # 1234
print(get_password("bloop", "bloop2"))         # None