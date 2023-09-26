day_of_week = input("What day of the week is today? ").capitalize()

print(day_of_week == "Monday")

if day_of_week == "Monday":
    print("Have a great start of the week!")
elif day_of_week == "Tuesday":
    print("It's Tuesday.")
#if day_of_week != "Monday":
else:
    print("Full speed ahead!")
print("This always runs.")
