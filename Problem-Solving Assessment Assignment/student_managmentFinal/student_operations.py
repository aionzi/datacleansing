# Importing function and exceptions for student ID validation and error handling
from validation import validate_student_id
from exceptions import InvalidIDException, DuplicateStudentIDException

# Importing the Undergraduate student model
from models.undergraduate import Undergraduate

# In-memory list to store all student objects
students = []

def add_student(student):
    """Adds a new student to the system after validation. Raises:
    DuplicateStudentIDException if the student ID already exists.
    InvalidIDException if student ID format is invalid.
    """
    if validate_student_id(student.get_student_id()):
        # Check for duplicate student ID
        for s in students:
            if s.get_student_id() == student.get_student_id():
                raise DuplicateStudentIDException("Student ID already exists.")
        # Append the valid, non-duplicate student to the list
        students.append(student)
    else:
        raise InvalidIDException("Invalid Student ID.")

def delete_student(student_id):
    """Deletes a student from the system using their student ID. Raises InvalidIDException if the student ID is invalid or not found.
    """
    if not validate_student_id(student_id):
        raise InvalidIDException("Invalid Student ID.")
    
    global students
    # Check if student with given ID exists
    if not any(s.get_student_id() == student_id for s in students):
        raise InvalidIDException("Student ID not found.")
    
    # Remove student with the matching ID
    students = [s for s in students if s.get_student_id() != student_id]

def update_student(student_id, new_course):
    """Updates the course information of a student. Raises the InvalidIDException if the student ID is invalid or not found."""
    if not validate_student_id(student_id):
        raise InvalidIDException("Invalid Student ID.")
    
    for s in students:
        if s.get_student_id() == student_id:
            # Update the course for the matching student
            s.update_course(new_course)
            return
    # Raise error if no matching student found
    raise InvalidIDException("Student ID not found.")

def list_students():
    """
    Returns a list of details for all students.
    list: A list of strings or dicts containing student details.
    """
    return [s.get_details() for s in students]
