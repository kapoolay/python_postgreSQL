# Magic number app

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":    # if you don't want to use the .lower() function, you can set this to be "user_input in ("y","Y")"
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:    # abs() function changes the value to be a positive number
        print("You are off by 1")
    else:
        print(f"Sorry, {user_number} is wrong.")
else:
    print("Maybe next time!")