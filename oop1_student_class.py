class Subject:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, first_name: str, last_name: str, year: int = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.grades: list = []
        self.subjects: list[Subject] = []

    def greet(self):
        print('Hi! My name is ' + self.first_name)

    def add_grade(self, grade: int):
        if grade > 10:
            raise ValueError('Grade must be less than or equal to 10')
        self.grades.append(grade)

    def average(self) -> float:
        return sum(self.grades)/len(self.grades)

    def add_course(self, subject: Subject):
        if len(self.subjects) == 6:
            raise ValueError('Student cannot have more than 6 subjects')
        self.subjects.append(subject)

