def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list")
else:                                               # If try runs successfully and no error happened, then run this
    print(f"The average grade is {average}.")
finally:
    print("This always runs no matter what!")

'''
Welcome to the average grade program.
Divisor cannot be 0.
There are no grades yet in your list
This always runs no matter what!
'''

#
# ## Without 'try' and 'except'
#
# print("Welcome to the average grade program.")
# average = divide(sum(grades), len(grades))
#
# print(f"The average grade is {average}.")
#
# '''
# Welcome to the average grade program.
# Traceback (most recent call last):
#   File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/31_errors_in_python/code.py", line 10, in <module>
#     average = divide(sum(grades), len(grades))
#   File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/31_errors_in_python/code.py", line 3, in divide
#     raise ZeroDivisionError("Divisor cannot be 0.")
# ZeroDivisionError: Divisor cannot be 0.
# '''