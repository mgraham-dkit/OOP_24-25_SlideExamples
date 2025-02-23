# This allows for forward referencing in type hints,
# i.e. we can type hint using the same type as the class we're in
# Here Student is used as a type hint on the rich comparison methods
from __future__ import annotations

class Student:
    # todo: docstrings
    """
        Class to model a Student. Student grades are held in a list.
        Each grade is held as a tuple structured as: (module_name (str), grade (a float))
        The highest grade across all created Student objects is stored in a static variable
        called top_grade.
    """
    # Static (shared) variable because it's created outside methods and doesn't include a reference to self.
    top_grade = None

    # Create a constructor to build a Student
    def __init__(self, id_num: str, name: str, year: int, grades: list[tuple[str, float]]=None):
        # The below is an example of a docstring for a method. This one outlines:
        #   what the method does
        #   the parameters taken in (what they are and what they're for)
        #   Note: self isn't included in the parameters as it's an implicit one; it won't be included in the call
        #   Any exceptions raised by the method (their types and any potential causes)

        """
            Create an instance of Student. If the new Student has a grade higher than the current top_grade
                for all Students, the top_grade is updated.

            Args:
                id_num (str)    : The id number of the student
                name (str)      : The name of the student
                year (int)      : The current college year of the student (Year must be between 1 and 4)
                grades (list[(str, float)]) : A list of the student's grades. (Defaults to None)
                (Duplicate module names are permitted. Grade values must be between 1 and 100).

            Raises:
                ValueError: Where the year, the length of a grade tuple or a grade value supplied are inappropriate.
                TypeError: Where grades are not provided as tuples or grade values are not provided as numbers
                (either float OR int)
        """

        # Store supplied id and name information
        self.id_num = id_num
        self.name = name

        # Check if the year is valid
        if year <= 0 or year > 4:
            # If it's not, then raise an exception to indicate the year is invalid
            # Remember to include (pass) a message to indicate what's gone wrong
            raise ValueError("Inappropriate year value supplied - Maximum of 4 years possible")
        # If the year provided is allowable, save it
        self.year = year

        # Set valid grades list if none provided
        if grades is None:
            grades = []
        # Create a variable to track the highest grade for THIS student
        student_max = ("None", -1)
        # Loop through all the supplied grade tuples
        for grade in grades:
            # Check if the current grade is not a tuple
            if not isinstance(grade, tuple):
                raise TypeError(f"Grades must be provided as tuples. Grade provided as: {grade}")
            # If there are not enough pieces in the grade to be valid (need 2 - a module name and a grade value)
            if len(grade) != 2:
                # Raise a ValueError to indicate it doesn't contain the correct number of pieces
                raise ValueError(f"Grades must be provided in format: (Module name, grade achieved). Grade provided as: {grade}")
            # If the grade value is not a number (either int OR float)
            if not isinstance(grade[1], int) and not isinstance(grade[1], float):
                # Raise a TypeError to indicate the grade value needs to be numeric
                raise TypeError(f"Grade value must be provided as a number (int or float). Grade provided: {type(grade[1])}")
            # If the grade value provided is too big or too small
            if grade[1] < 0 or grade[1] > 100:
                # Raise a ValueError to indicate the grade needs to be between 1 and 100
                raise ValueError(f"Grade cannot be less than 0 or over 100. Grade provided: {grade[1]}")

            # If all the validation checks pass for this grade,
            # check if it's higher than the current max for this student
            # If it is, then update the current max
            if grade[1] > student_max[1]:
                student_max = grade

        # If all validation checks pass for EVERY grade, then save the list of grades as the student's grades
        # (Remember, the only way we could get to here is if we haven't raised any exceptions,
        # so the validation checks must all have passed)
        self.grades = grades
        # If this is the first Student created, the top_grade hasn't been changed from the default yet
        # (and is still None)
        if Student.top_grade is None:
            # Set this student's highest grade to be the highest grade for all students
            Student.top_grade = student_max
        # If this student's grade is higher than the current top grade
        elif student_max[1] > Student.top_grade[1]:
            # Set this student's highest grade to be the highest grade for all students
            Student.top_grade = student_max

    def __eq__(self, other: object) -> bool | type(NotImplemented):
        if not isinstance(other, Student):
            return NotImplemented

        # Case-insensitive comparison of id as ID shouldn't be case-sensitive
        return self.id_num.lower() == other.id_num.lower()

    # Don't need to implement ne as python implements it based on provided __eq__

    def __hash__(self) -> int:
        # case-insensitive hashing of id number as id shouldn't be case-sensitive
        return hash(self.id_num.lower())

    def __repr__(self) -> str:
        """Returns a string representation of all data in the Student class (includes variable names)"""
        return f"Student(id={self.id_num}, name={self.name}, year={self.year}, grades={self.grades})"

    def __str__(self) -> str:
        return f"{self.id_num} - {self.name} (Y{self.year})"

    def __format__(self, format_spec: str) -> str:
        match(format_spec.lower()):
            case "short":
                return f"{self.id_num} - {self.name}"
            case "full":
                grades = "\n\t".join(f"{grade [0]} - {grade[1]}" for grade in self.grades)
                return f"{self.id_num} - {self.name} \nYear {self.year} grades: \n\t{grades}"
            case _:
                return str(self)

    def __lt__(self, other: Student) -> bool | NotImplemented:
        if not isinstance(other, Student):
            return NotImplemented

        # Compare id number values without considering case
        return self.id_num.lower() < other.id_num.lower()

    def __le__(self, other: Student) -> bool | NotImplemented:
        if not isinstance(other, Student):
            return NotImplemented

        # Compare id number values without considering case
        return self.id_num.lower() <= other.id_num.lower()

    def __gt__(self, other: Student) -> bool | NotImplemented:
        if not isinstance(other, Student):
            return NotImplemented

        # Compare id number values without considering case
        return self.id_num.lower() > other.id_num.lower()

    def __ge__(self, other: Student) -> bool | NotImplemented:
        if not isinstance(other, Student):
            return NotImplemented

        # Compare id number values without considering case
        return self.id_num.lower() >= other.id_num.lower()
