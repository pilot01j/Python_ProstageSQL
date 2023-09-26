from operator import itemgetter


def devide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 2, operator=devide)
print(result)

print("----------------------------------------------------------")


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could nor find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 20},
    {"name": "Adam Wool", "age": 25},
    {"name": "Anne Pun", "age": 27}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend["name"] ))
print(search(friends, "Rolf Smith", itemgetter("name") ))