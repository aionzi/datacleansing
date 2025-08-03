def validate_student_id(student_id):
    """Validates that the student ID is a positive integer.
    Arguments taken are student_id to validate.

    Returns bool True if the ID is a positive integer, False otherwise.
    """
    return isinstance(student_id, int) and student_id > 0
