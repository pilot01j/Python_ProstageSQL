def hello():
    print("Hello")


hello()
print("------------------------------------------------------------------")
print("Welcome to the age in seconds program!")


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f" Your age in seconds is : {age_seconds:_.0f}.")


user_age_in_seconds()
print("Goodbye!")
print("------------------------------------------------------------------")
friends = []
def add_friend():
    friends.append("Rolf")
    
add_friend()
add_friend()
add_friend()
print(friends)
