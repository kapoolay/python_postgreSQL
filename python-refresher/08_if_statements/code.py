day_of_week = input("What day of the week is it today?").lower()

if day_of_week == "monday":    # monday check
    print("Have a great start to your week!")
elif day_of_week == "tuesday":    #tuesday check
    print("I can't believe it's only Tuesday!")
elif day_of_week in ("friday", "saturday", "sunday"):    #weekend check
    print("Have a great weekend!")
elif day_of_week in ("thursday", "wednesday"):    #midweek check
    print("Full speed ahead!")
else:    # day of week check
    print("That is not a day of the week!")

#print("This always runs.")