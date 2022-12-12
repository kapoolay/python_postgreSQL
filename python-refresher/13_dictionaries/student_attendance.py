student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# loop thru the dictionary and print out each student's attendance
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}%")

# loops through both keys and values using .items()
for key, value in student_attendance.items():    # we use .items()
    print(f"{key}: {value}%")

# loops thru keys using .keys()
for key in student_attendance.keys():
    print(key)

# loops thru values using .values()
for value in student_attendance.values():
    print(value)


# check if a key exists in dictionary using "in"
if "Kevin" in student_attendance:
    print(f"Kevin: {student_attendance['Kevin']}")
else:
    print("Kevin does not exist.")

# calculate the average values
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

attendance_values = student_attendance.values()
print(f"Average: {sum(attendance_values) / len(attendance_values)}")
