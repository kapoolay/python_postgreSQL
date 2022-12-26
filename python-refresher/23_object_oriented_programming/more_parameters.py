class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (90, 90, 93, 78, 90))

print(student.name)
## Bob
print(student2.name)
## Rolf

print(student.average_grade())    # print(Student.average_grade(student2))
## 92.2
print(student2.average_grade())    # print(Student.average_grade(student2))
## 88.2