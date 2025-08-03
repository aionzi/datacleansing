# exceptions.py

#exception raised when a student ID is invalid
class InvalidIDException(Exception):
    pass

#exception raised when a student ID already exists in the system
class DuplicateStudentIDException(Exception):
    pass
