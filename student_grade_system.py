# Student Grade Management System - by Fathimath Nasreena K
# Project 2 - Python Practice for WFH Jobs

students = {}

def add_student(name, marks):
    students[name] = marks
    print(f"Added student: {name}")

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

def view_all_students():
    if not students:
        print("No students added yet!")
        return
    print("\n--- Student Report ---")
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        grade = calculate_grade(marks)
        print(f"Name: {name} | Marks: {marks} | Avg: {avg:.1f} | Grade: {grade}")

def topper():
    if not students:
        return
    top_name = ""
    top_avg = 0
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        if avg > top_avg:
            top_avg = avg
            top_name = name
    print(f"\nTopper: {top_name} with {top_avg:.1f}%")

# Main Program
while True:
    print("\n1. Add Student | 2. View All | 3. Find Topper | 4. Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        name = input("Student Name: ")
        m1 = int(input("Mark 1: "))
        m2 = int(input("Mark 2: "))
        m3 = int(input("Mark 3: "))
        add_student(name, [m1, m2, m3])
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        topper()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
