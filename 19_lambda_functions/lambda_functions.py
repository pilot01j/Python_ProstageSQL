def add(x, y):
    return x + y

print(add(3, 7))
print("----------------------------------------------------------")
print((lambda x, y: x + y)(3, 7))

print("----------------------------------------------------------")
def double(x):
    return x * 2

sequence = [1, 3 , 9]
doubled = [double(x) for x in sequence]
print(doubled)
print("----------------------------------------------------------")
doubled_map = list(map(double, sequence))
print(doubled_map)
print("----------------------------------------------------------")
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)
print("----------------------------------------------------------")
doubled_map = list(map(lambda x: x * 2, sequence))
print(doubled_map)

