##Having a parameter in the function requires you to have an argument when calling the function and vice versa

#this function doesn't have parameters
def say_hello():
    print("Hello!")

say_hello("Bob")    #passing an argument to a function that has no parameters will produce an error
# TypeError: say_hello() takes 0 positional arguments but 1 was given


#having a parameter in the function
def say_hello(name):
    print(f"Hello, {name.title()}!")

say_hello("kevin")
# Hello, Kevin!


