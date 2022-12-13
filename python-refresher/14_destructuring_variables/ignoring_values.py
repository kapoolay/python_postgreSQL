people =[
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Ignoring values, we can use "_" in place of a variable name
# we only want the name and profession
for name, _, profession in people:
    print(f"Name: {name}, Profession: {profession}")