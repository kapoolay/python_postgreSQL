# DO NOT USE PARAMETER VALUES THAT ARE MUTABLE
# Stick to immutable ones like int, str, floats, booleans, tuples etc..

from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
rolf = Student("rold")

bob.take_exam(90)
bob.take_exam(70)

print(bob.grades)       # [90, 70]
print(rolf.grades)      # []