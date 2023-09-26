user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "01234"

# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"
# print(secure_get_admin())

def secure_function(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            print(f" No admin permision for {user['username']}.")
    return secure_function

get_admin_password = secure_function(get_admin_password)

print(get_admin_password())