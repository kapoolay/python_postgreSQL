# Ask users for their age
# Tell them how many months their age equals to

age = int(input("How old are you: "))
#age_years = int(age)    # simplify code by adding int() function into the input
age_months = age * 12
age_days = age * 365
age_hours = age * 8760
age_seconds = age * 31536000

# Months (12 months in a year)
print(f"Your age, {age}, is equal to {age_months} months.")

# Days (365 days in a year)
print(f"Your age, {age}, is equal to {age_days} days.")

# Hours (8760 hours in a year)
print(f"Your age, {age}, is equal to {age_hours} hours.")

# Seconds (31536000 seconds in a year)
print(f"Your age, {age}, is equal to {age_seconds} seconds.")
