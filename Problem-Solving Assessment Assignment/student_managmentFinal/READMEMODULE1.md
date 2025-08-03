#TASK 1 : Student Management System

This is a student management system that used CRUD (Create, Read, Update and Delete) operations on student records. It supports both regular students and undergraduate students. The system stores student records in JSON and CSV files, allowing the program to retain data.


#Installation
1. *Extract the project*: Download and unzip the folder anywhere on your computer.
2. *Python Version*: Make sure you’re using Python 3.8+ (This was tested on Python 3.12) 
3. *Run the Project*: Run the program through the `main.py` file. To run go to your project folder in your termainl and run:
    `python main.py`

#Features
- *CRUD operations*: Add, update, read and delete Students and Student data.
- *Storage*: Reads and writes to CSV and JSON files for storing Student data.
- *Validation*: Validates Student data including ID, year, course, handles duplicate IDs and if the user wants to manipulate a Student that is not present in the database.
- *Exceptions*: Raises custom exceptions where a student attribute may be invalid; ensuring data integrity.
- *Student Objects*: `Student` and `Undergraduate` objects are used to store the students locally to manipulate them effectively. Student IDs are encapsulated to protect sensitive attributes. The Undergraduate class inherits from the `Student` super class

#File Structure
- `main.py`: Entry point for the application. 
- `student_operations.py`: Contains core functionalities. 
- `database.py`: Stores student records. 
- `validation.py`: Validates student data.
- `storage.py`: Handles file operations.
- `exceptions.py`: Defines custom exceptions used across the system.
- `models/student.py`: `Student` base class with encapsulation.
- `models/undergraduate.py`: `Undergraduate` subclass. 


#Usage
To start the program run the `main.py` file. To run go to your project folder in your termainl and run:
    `python main.py`
Upon running this file, you will be presented with an interactive menu, where you will be prompted with:
- Adding a student
- Deleting a student
- Updating a student
- Listing all students
- To exit the program

All interactions are guided, no setup is required.

#Error Handling

The system uses custom exceptions to handle different error scenarios:
- *InvalidIDException*: Raised when a student ID is invalid.
- *InvalidYearException*: Raised when the year is not a valid integer.
- *InvalidCoursesException*: Raised when a course name is invalid.
- *DuplicateStudentIDException*: Raised when attempting to add a student with a duplicate ID.
- *StudentNotFoundException*: Raised when trying to update or delete a student that doesn’t exist.