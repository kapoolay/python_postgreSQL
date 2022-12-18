def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 3)
print(result)
## 5.0

# Recommendation is not to 'return' multiple, different data types (i.e. integer and string)
result = divide(15, 0) * 5
print(result)
## You fool!You fool!You fool!You fool!You fool!