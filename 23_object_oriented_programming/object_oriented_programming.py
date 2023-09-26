student = {"name": "Ralf", "grades": (89, 90, 75, 80)}

def average(sequences):
    return sum(sequences) / len(sequences)

print(average(student["grades"]))
print("----------------------------------------------------------")

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average_new(self):
        return sum(self.grades) / len(self.grades)

student = Student("EDY", (10, 50, 80, 99))
print(student.name)
print(student.grades)
print(Student.average_new(student))

student_2 = Student("Ejhhj", (100, 59, 90, 99))
print(student_2.name)
print(student_2.grades)
print(student_2.average_new())