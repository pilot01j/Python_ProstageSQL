def add(x, y):
    print(x + y)

add(5, 8)
result = add(5, 8)
print(result)
# functions without return , return None
print("----------------------------------------------------------")
def add(x, y):
    return x + y

result = add(8, 8)
print(result)
print("----------------------------------------------------------")
def add(x, y):
    print("Before return")
    return x + y
    print("After return")  # it is not executed

result = add(8, 8)
print(result)
print("----------------------------------------------------------")
