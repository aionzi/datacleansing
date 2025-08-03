import json  # Importing the JSON module for reading/writing JSON data

# Importing the Undergraduate class to reconstruct student objects from saved data
from models.undergraduate import Undergraduate

def save_students_to_file(students, filename='students.json'):
    """Saves a list of student objects to a JSON file, Arguments taken:
    students (list): List of Undergraduate student objects.
    filename (str): Name of the JSON file to save to (default is 'students.json').
    """
    with open(filename, 'w') as f:
        # Convert each student object to a dictionary and dump the list to the file
        json.dump([s.__dict__ for s in students], f)

def load_students_from_file(filename='students.json'):
    """Loads student data from a JSON file and returns a list of Undergraduate objects. Arguments Taken:
    filename (str): Name of the JSON file to read from (default is 'students.json').
    Returns a list of Undergraduate student objects.
    """
    try:
        with open(filename, 'r') as f:
            # Load JSON data and convert each dictionary into an Undergraduate object
            return [Undergraduate(**data) for data in json.load(f)]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []
