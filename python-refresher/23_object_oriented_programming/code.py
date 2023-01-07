# Normal Syntax

student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

# print(average(student["grades"]))
## 88.0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OBJECT ORIENTED PROGRAMMING SYNTAX
# Call a class
# Init method runs --> def __init__(self)
# and what you get back is the object ("self") you created
# Main Point: Define another method, such as the average method, inside the class AND this method will take 'self' as a parameter

# # KEY BENEFIT of OBJECT ORIENTED PROGRAMMING
# You can define methods inside a class, that use the object that was initially created by the __init__ method within them. So that you don't
# have to keep track of multiple pieces of data and the object themselves can contain the method that you want to use inside it. All the data
# and methods are in one place --> Inside the class


class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    ## Defining method inside a class has to take a parameter
    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()    # student is the same as the object created in the Student class --> "self".
                       # Using "()" is a syntax to relate it to the object

# print(student.name)    # accessing the 'name' property, of our 'student' variable, which is 'self' we created earlier
## Rolf

# print(student.grades)
## (89, 90, 93, 78, 90)

print(Student.average_grade(student))    # we are calling the 'average' method from the 'Student' class, using
## 88.2                                  # the 'student' object which is the object in the class Student()


# You can rewrite is this way to make it shorter, but 'student = Student()' needs to be defined prior
print(f"Average Grade: {student.average_grade()}")
## 88.2


# Test to change name in the Student class
student.name = "Kevin"
print(f"New Name: {student.name}")
## Kevin