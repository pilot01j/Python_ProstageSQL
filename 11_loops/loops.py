number = 7
while True:
    user_input = input("Would you like to play? Y/n: ")
    if user_input == "n":
        break
    user_numer = int(input("Guess our number: "))
    if user_numer == number:
        print("You guessed correctly!")
        break
    elif number - user_numer in (1, -1):
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

print("------------------------------------------------------------------")
friends = ["Marin", "Vadim", "Ion"]
for friend in friends:
    print(f"{friend} is my friend.")

for x in range(len(friends)):
    print(f"{friends[x]} is not my friend.")
print("------------------------------------------------------------------")
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)
for grade in grades:
    total = total + grade
print(total)
print(total/amount)
print("Using sum func: ", sum(grades))
