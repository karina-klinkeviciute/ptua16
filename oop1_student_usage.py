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


john.grades = [1, 5, 6, 7, 9]

print(john.grades)

john.grades.append(2)

john.add_grade(10)

print(john.grades)

# john.add_grade(15)

print(john.average())

for subject in john.subjects:
    print(subject.name)

