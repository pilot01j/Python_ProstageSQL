i = 5
x = (5, 11)  # tuple
y = 5, 11  # tuple to
a, b = y
print(a, b)
print("------------------------------------------------------------------")
student_attendance = {"Doina": 100, "Jana": 80, "Susana": 90}
print(list(student_attendance.items()))

for key, value in student_attendance.items():
    print(f"{key}: {value}")
print("------------------------------------------------------------------")
people = [("Marin", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecture")]
for name, age, profesion in people:
    print(f"Name: {name}, Age: {age}, Profession: {profesion}.")
print("------------------------------------------------------------------")
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}.")
print("------------------------------------------------------------------")
new_person = ("Jon", 42, "Driver")
new_name, _, new_profession = new_person
print(new_name, new_profession)
print("------------------------------------------------------------------")
head, *trial = [1, 2, 3, 4, 5]
print(head)
print(trial)
print("------------------------------------------------------------------")
*head, trial = [1, 2, 3, 4, 5]
print(head)
print(trial)
print("------------------------------------------------------------------")
*head, trial = [1, 2, 3, 4, 5]
print(*head)  # not a list
print(trial)
