from __future__ import annotations
from student_exceptions import GradeError

class Student:
    top_grade = None

    def __init__(self, id_num, name, year, grades=None):
        self.id_num = id_num
        self.name = name

        if year < 0 or year > 4:
            raise ValueError("Inappropriate year value supplied - Maximum of 4 years possible")
        self.year = year

        student_max = ("None", -1)
        if grades is None:
            grades = []
        for grade in grades:
            if not isinstance(grade, tuple):
                # Instead of raising standard exceptions, we raise a custom exception specific to our own logic
                raise GradeError(f"Grades must be provided as tuples. Grade provided as: {grade}")
            if len(grade) != 2:
                raise GradeError(f"Grades must be provided in format: (Module name, grade achieved). Grade provided as: {grade}")
            if not isinstance(grade[1], int) and not isinstance(grade[1], float):
                raise GradeError(f"Grade value must be provided as a number (int or float). Grade provided: {type(grade[1])}")
            if grade[1] < 0 or grade[1] > 100:
                raise GradeError(f"Grade cannot be less than 0 or over 100. Grade provided: {grade[1]}")

            if grade[1] > student_max[1]:
                student_max = grade

        self.grades = grades
        if Student.top_grade is None:
            Student.top_grade = student_max
        elif student_max[1] > Student.top_grade[1]:
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
