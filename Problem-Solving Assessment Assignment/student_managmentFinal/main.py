# Importing custom exceptions for error handling
from exceptions import DuplicateStudentIDException, InvalidIDException

# Importing CRUD operations for student management
from student_operations import add_student, delete_student, update_student, list_students

# Importing the Undergraduate student model
from models.undergraduate import Undergraduate

# Importing functions to load and save students to a file
from storage import load_students_from_file, save_students_to_file

def main():
    # Load existing students from file into a global list
    global students
    students = load_students_from_file()

    while True:
        # Displaying the menu
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. List Students")
        print("5. Exit")
        
        # Taking user input for menu choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Adding a new student
            try:
                student_id = int(input("Enter Student ID: "))  # ID must be an integer
                name = input("Enter Name: ")
                course = input("Enter Course: ")
                minor = input("Enter Minor: ")
                year = int(input("Enter Year: "))
                # Create an Undergraduate object
                student = Undergraduate(student_id, name, course, minor, year)
                add_student(student)  # Add student to list
                print("Student added successfully.")
            except (ValueError, InvalidIDException, DuplicateStudentIDException) as e:
                # Catching input conversion errors, ID format issues, or duplicates
                print(f"Error: {e}")

        elif choice == '2':
            # Deleting a student by ID
            try:
                student_id = int(input("Enter Student ID to delete: "))
                delete_student(student_id)
                print("Student deleted successfully.")
            except (ValueError, InvalidIDException) as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Updating a student's course info
            try:
                student_id = int(input("Enter Student ID to update: "))
                new_course = input("Enter new Course: ")
                update_student(student_id, new_course)
                print("Student updated successfully.")
            except (ValueError, InvalidIDException) as e:
                print(f"Error: {e}")

        elif choice == '4':
            # Listing all students
            print("Listing Students:")
            for details in list_students():
                print(details)

        elif choice == '5':
            # Saving students to file and exiting the program
            save_students_to_file(students)
            print("Exiting the system.")
            break

        else:
            # Handling invalid menu input
            print("Invalid choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
