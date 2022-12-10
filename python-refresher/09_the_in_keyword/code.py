# check to see if a name is in a list
friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

# check to see if a user's input movie is in a set
movies_watched = {"the matrix", "green book", "her"}
user_movie = input("Enter something you've watched recently: ").lower()

print(user_movie in movies_watched)


# using the 'in' within the 'if' statement
movies_watched = {"the matrix", "green book", "her"}
user_movie = input("Enter something you've watched recently: ").lower()

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")