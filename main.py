class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # self.stud_l = []


    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lekt(self, lektor, course, grade):
        if isinstance(lektor, Lecturer) and course in self.courses_in_progress and course in lektor.courses_attached:
            if course in lektor.grades:
                lektor.grades[course] += [grade]
            else:
                lektor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_comparison (self, student):
        if get_average(self.grades) == get_average(student.grades):
            print('Равны')
        if get_average(self.grades) > get_average(student.grades):
            print(
                f'Средние оценки {self.surname} {self.name} {get_average(self.grades)} лучше чем {get_average(student.grades)} у {student.surname} {student.name}')
        else:
            print(
                f'Средние оценки {student.surname} {student.name} {get_average(student.grades)}  лучше чем {get_average(self.grades)} у {self.surname} {self.name}')
        return

    def __str__(self):
            lec = f"""Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за дз: {get_average(self.grades)}
Курсы в процессе изучения: {self.courses_in_progress}
Завершенные курсы: {self.finished_courses}
"""
            return lec


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        rev = f"""Имя: {self.name} 
Фамилия: {self.surname}"""
        return rev

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_comparison(self, lektor):
        if get_average(self.grades) == get_average(lektor.grades):
            print('Равны')
        if get_average(self.grades) > get_average(lektor.grades):
            print(f'Средние оценки {self.surname} {self.name} {get_average(self.grades)} лучше чем {get_average(lektor.grades)} у {lektor.surname} {lektor.name}')
        else:
            print(f'Средние оценки {lektor.surname} {lektor.name} {get_average(lektor.grades)}  лучше чем {get_average(self.grades)} у {self.surname} {self.name}')
        return

    def __str__(self):
        lec = f"""Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за лекции: {get_average(self.grades)}
"""
        return lec

def get_average(grade_l):
    num = 0
    null = 0
    iter = 0
    for i in grade_l.values():
        for p in i:
            if null < p:
                num += p
                iter +=1
            else:
                continue
    res = num / iter
    return res















klubnickin = Lecturer('Grishka', 'Klubnickin')
klubnickin.courses_attached += ['Python']


arbuzov = Lecturer('Andrey', 'Arbuzov')
arbuzov.courses_attached += ['JS']


tomatov = Student('Ruslan', 'Tomatov', 'm')
tomatov.finished_courses += ['OOP']
tomatov.courses_in_progress += ['Python', 'JS']
tomatov.rate_lekt(klubnickin, 'Python', 8)
tomatov.rate_lekt(arbuzov, 'JS', 7)


ogurcova = Student('Natalia', 'Ogurcova', 'w')
ogurcova.finished_courses += ['JS']
ogurcova.courses_in_progress += ['Python', 'OOP']
ogurcova.rate_lekt(klubnickin, 'Python', 3)


persikov = Reviewer('Valera', 'Persikov')
persikov.courses_attached += ['JS']
persikov.rate_hw(tomatov, 'JS', 10)
persikov.rate_hw(tomatov, 'JS', 8)
persikov.rate_hw(ogurcova, 'JS', 5)
persikov.rate_hw(ogurcova, 'JS', 10)


yablokov = Reviewer('Stanislav', 'Yablokov')
yablokov.courses_attached += ['Python']
yablokov.rate_hw(tomatov, 'Python', 6)
yablokov.rate_hw(tomatov, 'Python', 7)
yablokov.rate_hw(ogurcova, 'Python', 5)
yablokov.rate_hw(ogurcova, 'Python', 8)


Lecturer.get_comparison(klubnickin, arbuzov)
print(arbuzov)
print(klubnickin)

Student.get_comparison(ogurcova, tomatov)
print(ogurcova)

stud_l = [tomatov.grades, ogurcova.grades]
grades = []

def get_averange_course_stud(stud_l, course):
    num = 0
    null = 0
    iter = 0
    for stud in stud_l:
        if course in stud:
            grades.append(stud[course])
            for i in grades:
                for p in i:
                    if null < p:
                        num += p
                        iter += 1
                    else:
                        continue
            res = num / iter
            grades.clear()
    return (f'По курсу {course} средняя оценка у студентов {res}')


print(get_averange_course_stud(stud_l, 'JS'))
print(get_averange_course_stud(stud_l, 'Python'))

lect_l = [klubnickin.grades, arbuzov.grades]
grades_lec = []

def get_averange_course_lect(lect_l, course):
    num = 0
    null = 0
    iter = 0
    for lect in lect_l:
        if course in lect:
            grades_lec.append(lect[course])
            for i in grades_lec:
                for p in i:
                    if null < p:
                        num += p
                        iter += 1
                    else:
                        continue
            res = num / iter
            grades_lec.clear()
    return (f'По курсу {course} средняя оценка у лекторов {res}')


print(get_averange_course_lect(lect_l, 'JS'))
print(get_averange_course_lect(lect_l, 'Python'))








