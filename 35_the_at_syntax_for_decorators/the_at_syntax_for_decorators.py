import functools

user = {"username": "jose", "access_level": "admin"}

def secure_function(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f" No admin permision for {user['username']}."
    return secure_function


@secure_function
def get_admin_password():
    return "01234"


print(get_admin_password.__name__)