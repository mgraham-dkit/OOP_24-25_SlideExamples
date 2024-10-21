class Staff:
    def __init__(self, fName, lName, dept):
        self.fName = fName
        self.lName = lName
        self.dept = dept

    def generate_email(self):
        dept = self.dept.replace(" ", "_")
        return f"{self.fName[0].lower()}{self.lName.lower()}.{dept.lower()}@workdomain.com"

    def display(self):
        print(f"Staff[fName={self.fName}, lName={self.lName}, dept={self.dept}]")


class PartTimeStaff(Staff):
    def __init__(self, fName, lName, dept, hours_worked, hourly_rate = 10.50):
        super().__init__(fName, lName, dept)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calc_wage(self):
        if self.hours_worked < 10:
            gross_pay = 10 * self.hourly_rate
        else:
            gross_pay = self.hours_worked * self.hourly_rate

        return gross_pay

    def display(self):
        super().display()
        print(f"PartTimeStaff[hours_worked={self.hours_worked}, hourly_rate={self.hourly_rate}]")


class FullTimeStaff(Staff):
    def __init__(self, fName, lName, dept, salary, benefits=None):
        super().__init__(fName, lName, dept)
        self.salary = salary
        if benefits is None:
            benefits = ["Health insurance"]
        self.benefits = benefits

    def add_benefit(self, new_benefit):
        if new_benefit not in self.benefits:
            self.benefits.append(new_benefit)
            return True
        return False

    def display(self):
        super().display()
        print(f"FullTimeStaff[salary={self.salary}, benefits={self.benefits}]")
