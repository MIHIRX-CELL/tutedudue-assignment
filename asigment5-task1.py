# Step 1: Create a dictionary with student names as keys and marks as values
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92,
    "Ethan": 88
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 and 4: Retrieve and display marks or show a message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks are {student_marks[student_name]}")
else:
    print(f"Student name '{student_name}' not found.")
