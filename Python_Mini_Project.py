# Python Mini Project
# STUDENT PERFORMANCE ANALYZER

# Creating an empty list:
students =[]

# Entry number of students:
n = int(input("Enter number of students: "))

# Collection student details:
for i in range(n):
    print("\nStudent",i + 1)
    name = input("Enter student name: ")
    marks =[]
    print("Enter marks in 5 subjects (out of 100): ")

    for j in range(5):
        m = float(input("Subject " + str(j + 1) + ": "))
        marks.append(m)

    # Calculating total and percentage:
    total = sum(marks)
    percentage = total / 5

    # Assigning the grades of students: 
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    # Store student details
    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }
    students.append(student)

# Find the topper of class.
topper = students[0]
for student in students:
    if student["percentage"] > topper["percentage"]:
        topper = student

# Atlast display the full report.
print("\n===== STUDENT PERFORMANCE REPORT =====")
for student in students:
    print("\nName:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", student["total"], "/ 500")
    print("Percentage:", student["percentage"], "%")
    print("Grade:", student["grade"])

print("\n===== TOPPER DETAILS =====")
print("Topper:", topper["name"])
print("Percentage:", topper["percentage"], "%")

print("\n===== ANALYSIS COMPLETE =====")
