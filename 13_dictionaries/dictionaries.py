friends = {'Rolf': 24, "Adam": 30, "Anne": 27}
print(friends)
print(friends["Anne"])

friends["Bob"] = 20
print(friends)
friends["Bob"] = 40
print(friends)
print("------------------------------------------------------------------")
new_friends = [
    {"name": "Marin", "age": 30},
    {"name": "Vadim", "age": 32},
    {"name": "Ion", "age": 20}
]
print(new_friends)
print(new_friends[0]["name"])
print("------------------------------------------------------------------")
student_attendance = {"Doina": 100, "Jana": 80, "Susana": 90}
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")
print("------------------------------------------------------------------")
for key, value in student_attendance.items():
    print(f"{key}: {value}")
print("------------------------------------------------------------------")
if "Doina" in student_attendance:
    print(f"Doina: {student_attendance['Doina']}")
else:
    print("Doina is not a student in this class.")
print("------------------------------------------------------------------")
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))



