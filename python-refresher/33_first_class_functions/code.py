def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
result2 = calculate(12, 0, operator=divide)

print(result)       # 5.0

print(result2)
'''
Traceback (most recent call last):
  File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/33_first_class_functions/code.py", line 11, in <module>
    result2 = calculate(12, 0, operator=divide)
  File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/33_first_class_functions/code.py", line 8, in calculate
    return operator(*values)
  File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/33_first_class_functions/code.py", line 3, in divide
    raise ZeroDivisionError("Divisor cannot be 0.")
ZeroDivisionError: Divisor cannot be 0.
'''

