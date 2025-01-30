from students import Student

def process_grades(grade_text: list[str]) -> list[tuple[str, float]]:
    grades = []
    for grade in grade_text:
        module, score = grade.split("__")
        grades.append((module, float(score)))

    return grades

def process_student(line: str) -> Student | None:
    line = line.strip()
    student_data = line.split("%%")
    if len(student_data) == 4:
        id_code = student_data[0]
        name = student_data[1]
        try:
            year = int(student_data[2])
            grade_data = student_data[3].split("~~")
            # Call function to parse the grade information
            student_grades = process_grades(grade_data)
            return Student(id_code, name, year, student_grades)
        except ValueError as e:
            print(f"Numeric type issue with student record: {line}")
            print(e)
    else:
        print(f"Inappropriate amount of data supplied for student: {line}")

    return None

def display_students(student_list: list[Student]) -> None:
    for student in student_list:
        # Print all students using the "full" format as defined in __format__
        print(format(student, "full"))

def process_student_file(student_file: str) -> list[Student]:
    students = []
    # This function lets the FileNotFoundError occur - it doesn't handle it
    # This is to allow the calling code to handle it and do the input re-entry aspect
    with open(student_file) as file:
        for line in file:
            # Call function to parse the student information
            s = process_student(line)
        if s:
            students.append(s)

    return students


students_list = None
while not students_list:
    filename = input("Please enter the filename for student data (including relative path): ")
    try:
        # Call function to process the file
        students_list = process_student_file(filename)
    # File could not be found - stop process and raise error
    except FileNotFoundError as e:
        print(f"No such file (\"{filename}\") was found. Please try again.")
