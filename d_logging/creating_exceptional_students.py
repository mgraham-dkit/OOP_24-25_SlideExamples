import json
import logging
import logging.config
from students import Student


# Configure the logging settings for the application
def configure_logging(logging_level: int) -> None:
    student_file_handler = logging.FileHandler(filename="student_log.txt", mode="a")
    student_file_handler.setLevel(logging.WARNING)

    # Add an extra handler to the configuration to send debug messages to the console
    # Note: This will ONLY kick in when the overall logging level is set to debug, otherwise they'll be ignored
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Configure the logging set up and assign handlers
    logging.basicConfig(format='%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(message)s]',
                        level=logging_level, handlers=[student_file_handler, console_handler])

def configure_logging_json() -> None:
    # Read in the json config
    with open("logging_config.json", "r") as f:
        config = json.load(f)

    # Apply logging configuration
    logging.config.dictConfig(config)


def parse_student(student_line: str) -> Student | None:
    student_data = student_line.split("%%")
    if len(student_data) == 4:
        id_num = student_data[0]
        name = student_data[1]
        try:
            year = int(student_data[2])
            grade_data = student_data[3].split("~~")
            grades = []
            for grade in grade_data:
                module, score = grade.split("__")
                grades.append((module, float(score)))
            return Student(id_num, name, year, grades)
        except ValueError as e:
            print(f"Numeric type issue with student record: {student_line}")
            logger.exception("Bad data provided")
    else:
        print(f"Inappropriate amount of data supplied for student: {student_line}")

    return None


def display_students(student_list: list[Student]) -> None:
    for s in student_list:
        print(format(s, "short"))



# configure_logging(logging.ERROR)
configure_logging_json()
logger = logging.getLogger(__name__)
valid_file = False
students = []

while not valid_file:
    try:
        filename = input("Please enter the filename for student data (including relative path): ")
        with open(filename) as file:
            valid_file = True
            for line in file:
                line = line.strip()
                student = parse_student(line)
                if student:
                    students.append(student)
                    print(f"Student {student} added to the list")

    except FileNotFoundError as e:
        print("No such file was found. Please try again.")
        logger.warning(f"Invalid filename provided: {filename}")

display_students(students)
