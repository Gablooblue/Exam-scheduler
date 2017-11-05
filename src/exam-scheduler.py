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

def output(color_index, classes, students):
    f = open("../index.html", "w")
    f.write("<html>")
    f.write("<h1>Exam schedules</h1>")
    f.write("<link rel = 'stylesheet' href = 'styles.css'")
    f.write("<body>")
    f.write("<table>")

    f.write("<tr>")
    f.write("<th>Exam time</th>")
    f.write("<th>Class/es</th>")
    f.write("</tr>")
    timestart = 7
    for i in range(max(color_index)):
        timeslot = []
        f.write("<tr>")
        f.write("<td>" + str(timestart + i) + ":00-" + str(timestart+ 1 + i) + ":00</td>")
        for j in range(len(classes)):
            if color_index[j] == i:
                timeslot.append("COURSE" + str(j + 1))
        same_time = ", ".join(timeslot)
        f.write("<td>" + same_time + "</td>")
        f.write("</tr>")
    f.write("</table>")
    f.write("</body>")
    f.write("</html>")

def main():
    classes = []
    students = []
    read(classes, students)
    color_index = [0] * len(classes)
    edges = [[0 for j in range(len(classes))] for i in range(len(classes))]

    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            for k in classes[i]:
                if k in classes[j]:
                    edges[i][j] = 1

    for i in range(len(edges)):
        for j in range(i+ 1, len(edges)):
            if edges[i][j] == 1:
                while color_index[i] == color_index[j]:
                    color_index[j] += 1

    output(color_index, classes, students)


    
main()
