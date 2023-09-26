# y have default values 8
def add(x, y=8):
    print(x + y)

add(x=10, y=5)
add(x=10)

# Error if you cal in such mode the functions
# add(x=10, 10)
print("------------------------------------------------------------------")
# you can't define the default value outside the def parameters

default_y = 2
def substraction(x, y=default_y):
    result = x - y
    print(result)

substraction(2)
default_y = 4
substraction(2)
