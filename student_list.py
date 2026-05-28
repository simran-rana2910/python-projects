student_list = []

def add_student():
    name = input("Enter student name: ")
    student_list.append(name)
    print("Student added successfully!")

def display_students():
    if len(student_list) == 0:
        print("Student list is empty.")
    else:
        print("Student List:")
        for student in student_list:
            print(student)

def search_student():
    name = input("Enter student name to search: ")

    if name in student_list:
        print("Student found.")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name to remove: ")

    if name in student_list:
        student_list.remove(name)
        print("Student removed successfully!")
    else:
        print("Student not found.")

while True:

    print("\n----- MENU -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        remove_student()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")