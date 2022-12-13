student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}    # dictionary

# turning this into a list because .items() doesn't quite return a list of tuples
# print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
