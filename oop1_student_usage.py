from oop1_student_class import Student, Subject


# A student should have a list of grades. It should also have a method for calculating average

subjects = {
    "mathematics": Subject("Mathematics"),
    "physics":  Subject("Physics"),
    "chemistry": Subject("Chemistry"),
    "art": Subject("Art"),
    "economics": Subject("Economics"),
    "science": Subject("Science"),
    "psychology": Subject("Psychology"),
}


john = Student('John', 'Doe')

john.greet()

john.add_course(subjects["mathematics"])
john.add_course(subjects["physics"])
john.add_course(subjects["chemistry"])
john.add_course(subjects["art"])
john.add_course(subjects["economics"])
john.add_course(subjects["science"])
# john.add_course(subjects["psychology"])


john._grades = [1, 5, 6, 7, 9]

print(john._grades)

john._grades.append(2)

john.add_grade(10)

print(john._grades)

# john.add_grade(15)

print(john.average())

for subject in john.subjects:
    print(subject.name)

john._grades.append(15)

print(john._grades)

print(john.get_grades())

print(john.average())

print(john._grades_count())

print(john._Student__grades_sum())
