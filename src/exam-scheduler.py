def read(classes, students):
    CLASSES_PATH = "../input/classes.txt"
    STUDENTS_PATH = "../input/students.txt"

    class_file = open(CLASSES_PATH, "r")
    for count, i in enumerate(class_file.readlines()):
        COURSE_PATH = "../input/COURSE" + str(count + 1) + ".txt"
        course_file = open(COURSE_PATH, "r")
        course = []

        for j in course_file.readlines():
            course.append(j.strip())

        course_file.close()
        classes.append(course)
    class_file.close() 

    students_file = open(STUDENTS_PATH, "r")

    for i in students_file.readlines():
        students.append(i.strip().split(","))

def main():
    classes = []
    students = []
    read(classes, students)
    edges = [[0 for j in i] for i in classes]

    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            for k in classes[i]:
                if k in classes[j]:
                    edges[i][j] = 1

    print(edges)
    
main()
