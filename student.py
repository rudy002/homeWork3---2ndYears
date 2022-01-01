class Course:
    def __init__(self, nameCourse, Grade=101):
        self.nameCourse = nameCourse
        self.Grade = Grade

    def setGrade(self, grade):
        if 0 <= int(grade) <= 100:
            self.Grade = grade
        else:
            raise ValueError("error. this grade is incorrect")

    #   from here this is function I added
    def GetNameCourse(self):
        return self.nameCourse

    def GetGrade(self):
        return self.Grade

    def __str__(self):
        return f'name COURSE :{self.nameCourse}, GRADE : {self.Grade}'

    def __repr__(self):
        return f'Course({self.nameCourse}:{self.Grade})'


class Student:
    def __init__(self, surname, ID):
        self.__ID = ID
        self.Surname = surname
        self.ListCourse = []

    def GetID(self):
        return self.__ID

    def addGrade(self, newCourse):
        if 0 <= newCourse.Grade <= 100:
            self.ListCourse.append(newCourse)
        else:
            raise ValueError("error. this grade is incorrect")

    #   from here, this is no request function form the homework

    def GetSurname(self):
        return self.Surname

    def CheckAndUptdate(self, course_check):
        for n in self.ListCourse:
            if n.GetNameCourse == course_check.nameCourse:
                n.SetGrade(course_check.Grade)
                return
        flag = Course(course_check.nameCourse)
        flag.setGrade(course_check.Grade)
        self.ListCourse.append(flag)

    def __repr__(self):
        return f'STUDENT : {self.Surname} NUMBER ID :{self.__ID} {self.ListCourse}'
