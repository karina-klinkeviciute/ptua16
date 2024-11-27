class Subject:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, first_name: str, last_name: str, year: int = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self._grades: list = []
        self.subjects: list[Subject] = []

    def greet(self):
        print('Hi! My name is ' + self.first_name)

    def add_grade(self, grade: int):
        if grade > 10:
            raise ValueError('Grade must be less than or equal to 10')
        self._grades.append(grade)

    def get_grades(self):
        return self._grades

    def __grades_sum(self):
        return sum(self._grades)

    def _grades_count(self):
        return len(self._grades)

    def average(self) -> float:
        return self.__grades_sum()/self._grades_count()

    def add_course(self, subject: Subject):
        if len(self.subjects) == 6:
            raise ValueError('Student cannot have more than 6 subjects')
        self.subjects.append(subject)

