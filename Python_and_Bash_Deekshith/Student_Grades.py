students = {}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Print all grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists. Use option 2 to update.")
        else:
            grade = input("Enter grade: ")
            students[name] = grade
            print("Student added.")

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        if len(students) == 0:
            print("No students yet.")
        else:
            for name, grade in students.items():
                print(name, ":", grade)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")