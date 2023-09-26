print("----------------------------------------------------------")


def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


multiply(1, 2, 3)
print(multiply(1, 2, 3, 10))
print("----------------------------------------------------------")


def add(x, y):
    return x + y


nums = [3, 9]
result = add(*nums)
print(result)
print("----------------------------------------------------------")

nums = {"x": 10, "y": 20}
result = add(nums["x"], nums["y"])
print(result)
print("----------------------------------------------------------")
nums = {"x": 100, "y": 200}
result = add(**nums)
print(result)
print("----------------------------------------------------------")


def multiply(args):
    result = tuple(element * element for element in args)
    return result


def add_new(*args):
    return sum(*args)


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    if operator == "+":
        return add_new(*args)
    else:
        return "No valid operator provided to apply()"

print(apply((1, 2, 3, 4), operator="+"))
print(apply((1, 2, 3, 4), operator="*"))

