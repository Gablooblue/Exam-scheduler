def main():
    classes = []
    students = []
    if not read(classes, students):
        print("Error: Place the program in the same folder as the input files")
        return

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
    style()

def read(classes, students):
    try:
        CLASSES_PATH = "classes.txt"
        STUDENTS_PATH = "students.txt"

        class_file = open(CLASSES_PATH, "r")
        for count, i in enumerate(class_file.readlines()):
            COURSE_PATH = "COURSE" + str(count + 1) + ".txt"
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
    except FileNotFoundError:
        return False 

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

def style():
    f = open('../styles.css', 'w')
    f.write('html')
    f.write('{')
    f.write('font-family: "Trebuchet MS", "sans-serif";')
    f.write('}')
    f.write('h1')
    f.write('{')
    f.write('text-align: center;')
    f.write('}')
    f.write('body')
    f.write('{')
    f.write('padding-top: 50px;')
    f.write('}')
    f.write('')
    f.write('table')
    f.write('{')
    f.write('width: 50%;')
    f.write('box-shadow: 4px 4px 5px #888888;')
    f.write('}')
    f.write('table, th, td')
    f.write('{')
    f.write('border-bottom: 1px solid grey;')
    f.write('border-collapse: collapse;')
    f.write('margin: 0 auto;')
    f.write('')
    f.write('}')
    f.write('tr:nth-child(even)')
    f.write('{')
    f.write('background-color: #F5F5F5;')
    f.write('}')
    f.write('')
    f.write('th')
    f.write('{')
    f.write('background-color:#07177E;')
    f.write('color: white;')
    f.write('}')
    f.write('')
    f.write('th, td')
    f.write('{')
    f.write('padding: 15px;')
    f.write('}')
    f.close()



    
main()
