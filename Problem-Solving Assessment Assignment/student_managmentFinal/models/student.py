class Student:
    """ Base class representing a student with basic attributes and operations.
    """

    def __init__(self, student_id, name, course, year):
        """
        initialise a new Student object.

        Arguments:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.
            course (str): Course the student is enrolled in.
            year (int): Year of study.
        """
        self.__student_id = student_id  # Private attribute for student ID
        self.name = name
        self.course = course
        self.year = year

    def get_student_id(self):
        """
        Returns the student's ID.
        """
        return self.__student_id

    def set_student_id(self, new_id):
        """
        Sets a new student ID if it's numeric.

        Arguments:
            new_id (str): The new student ID as a string.

        Raises:
            ValueError: If new_id is not numeric.
        """
        if new_id.isdigit():
            self.__student_id = int(new_id)
        else:
            raise ValueError("Student ID must be numeric!")

    def update_course(self, new_course):
        """
        Updates the student's course information.

        Args:
            new_course (str): The new course name.
        """
        self.course = new_course

    def get_details(self):
        """
        Returns a string containing basic student details.
        """
        return f"ID: {self.__student_id}, Name: {self.name}, Course: {self.course}"
