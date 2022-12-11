number = 7
##user_input = input("Would you like to play? (Y/n) ")

##while user_input != "n":
while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break    # this stops the infinite loop

    # if user types anything other than "n", we continue on with the next line of code
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:    # abs() function changes the value to be a positive number
        print("You are off by 1")
    else:
        print(f"Sorry, {user_number} is wrong.")

    print("Thanks for playing!")

##    user_input = input("Would you like to play? (Y/n) ")
