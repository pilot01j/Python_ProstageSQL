def named(**kwargs):  # accept dictionary elements
    print(kwargs)


named(name="Bob", age=42)
print("----------------------------------------------------------")
def named_new(name, age):
    print(name, age)

details = {'name': "Jon", 'age': 45}
named_new(**details)

print("----------------------------------------------------------")
details_new = {'name': "Jonatan", 'age': 15}
named(**details_new)

print("----------------------------------------------------------")
def print_nicely(**kwargs):
    named(**kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_nicely(name="Sebastian", age=25)
print("----------------------------------------------------------")
def both (*args, **kwargs):
    print(args)
    print(kwargs)
both(1, 2, 3,name="Siri", age=25)
print("----------------------------------------------------------")









