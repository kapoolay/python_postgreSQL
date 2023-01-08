# Methods with 2 underscores on each side are called special methods AKA "magic methods"
# __init__ | __str__ | __repr__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # "__str__" method turns your object into a string
    # print a nice easy to read string for users
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # "__repr__" method --> goal of this method is to be un-ambiguous
    # Returns a string that allows us to recreate the original object very easily
    # Used in other places like Python debugger
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"
        # <Tells programmers to read this string here, we are printing out an object>

bob = Person("Bob", 35)

print(bob)
## Bob is 35 years old.

print(bob.__repr__())
## <Person(Bob, 35)>