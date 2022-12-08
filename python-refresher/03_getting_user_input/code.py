# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ask for user's name
# name = input("Enter your name: ")
# print(name.title())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Doing maths with user input

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input) # The input() function ALWAYS returns a string, so you need to convert it into an INT
square_meters = square_feet / 10.8

# print(square_meters)
#print(f"{square_feet} sq. ft. is to {round(square_meters,2)} sq. meters")    # round(variable,decimal places) rounds the value to specified decimal
print(f"{square_feet} sq. ft. is to {square_meters:.2f} sq. meters")    # {number:.2f} rounds the value to 2 decimal places