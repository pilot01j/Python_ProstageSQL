def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be 0.")
        return
    return dividend / divisor


divide(15, 0)
print("----------------------------------------------------------")
grades = []

print("Welcome o the average grade program.")
average = divide(sum(grades), len(grades))
print(f"The average grade is {average}.")
print("----------------------------------------------------------")


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


grades = []

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are not grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank, you!")


print("----------------------------------------------------------")




