# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Instance Method
# Used for most things
# Produce an action to use the data inside the object you create
# Call a method to modify data inside {self} or {object}

class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

test = ClassTest()
test.instance_method()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Class Method
# Used often as factories

class ClassTest:
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}r")

ClassTest.class_method()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Static Method
# Used to place a method inside a class, bc you feel like it belongs there
# Put that method in there bc it makes sense logically, for code organization

class ClassTest:
    @staticmethod
    def static_method():
        print("Called static_method")

ClassTest.static_method()
