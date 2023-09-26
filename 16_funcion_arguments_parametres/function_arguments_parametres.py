def add(x, y):
    result = x + y
    print(result)


add(3, 4)
print("------------------------------------------------------------------")
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello("Bob", "Smith")
say_hello(surname="Black", name="Jack")
print("------------------------------------------------------------------")
def devide(devided, divisor):
    if divisor != 0:
        print(devided / divisor)
    else:
        print("You fool!")

devide(15, 0)
devide(15, 5)
devide(devided=0, divisor=15)
