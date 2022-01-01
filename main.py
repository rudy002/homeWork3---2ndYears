from student import Course, Student

#   nameFile = input("enter the name file you want open")
nameFile = "School.txt"


def checkFileExist(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        print("file not found ERROR1")
        return False
    except IOError as e:
        print("file not found ERROR2")
        return False


checkFileExist(nameFile)

file = open(nameFile)
student = file.read().splitlines()

list_student = []
all_student = []
for n in student:
    name_student = n.split("    ")[0]
    ID_student = n.split("    ")[1]
    obj_student = Student(name_student, ID_student)
    all_course_student = n.split("    ")[2].split(";")
    for m in all_course_student:
        name_course = m.split("#")[0]
        grade_course = int(m.split("#")[1])
        one_Course = Course(name_course)
        one_Course.setGrade(grade_course)
        obj_student.CheckAndUptdate(one_Course)

    list_student.append(obj_student)  # list of object student

print(list_student)

search = []
while True:
    answer = input("choose answer please\n1- average one Student\n2- average one Course\n3- average all Student\n4- "
                   "Exit")
    if int(answer) == 1:
        search = input("enter the name of the student you want check her Average")
        only_one_student = next((x for x in list_student if x.Surname == search), None)
        print((sum(list(map(lambda x: x.GetGrade(), only_one_student.ListCourse)))) / len((list(map(lambda x: x.GetGrade(), only_one_student.ListCourse)))))

    elif int(answer) == 2:
        pass
    elif int(answer) == 3:
        pass
    elif int(answer) == 4:
        break
    else:
        pass

print("End of program. thank you")
