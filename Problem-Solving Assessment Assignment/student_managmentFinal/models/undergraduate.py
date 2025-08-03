# Importing the base Student class
from models.student import Student

# Subclass representing an undergraduate student
class Undergraduate(Student):
    def __init__(self, student_id, name, course, minor, year):
        """
        initialise an Undergraduate student.

        Arguments taken:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.
            course (str): Major course of study.
            minor (str): Minor subject.
            year (str): Year of study.
        """
        # initialise attributes from the parent Student class
        super().__init__(student_id, name, course, year)
        self.minor = minor  


    def get_details(self):
        """
        Returns a formatted string containing all student details.
        """
        return f"ID: {self.get_student_id()}, Name: {self.name}, Course: {self.course}, Minor: {self.minor}, Year: {self.year}"
