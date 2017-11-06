def main():
    #Initializing lists for file read
    classes = []
    students = []

    #Reads input files
    if not read(classes, students): #If read is unsuccessful
        print("Error: Place the program in the same folder as the input files")
        return

    color_index = [0] * len(classes) #Used numbers instead of colors

    #Creating an adjacency matrix
    edges = [[0 for j in range(len(classes))] for i in range(len(classes))]

    #Iteratates through half of the matrix
    #since the other half is just symmetric to this one
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            for k in classes[i]: #Goes through every class in class[i]
                if k in classes[j]: #If they both have the same class
                    edges[i][j] = 1 #Set edge to one
                    break

    #Iterates through half of the adjacency matrix again
    for i in range(len(edges)):
        for j in range(i+ 1, len(edges)):
            if edges[i][j] == 1: #Vertices share an edge
                while color_index[i] == color_index[j]: #Change color until unique
                    color_index[j] += 1

    output(color_index, classes, students) #Creates HTML file
    style() #Creates CSS file
    print("Open index.html to view schedule")

'''
    @params: list of classes and students
    @returns: True or False (depending on read success)

    Reads all the input files and puts them in lists
'''
def read(classes, students):
    try:
        #Initializing path constants
        CLASSES_PATH = "classes.txt"
        STUDENTS_PATH = "students.txt"

        class_file = open(CLASSES_PATH, "r")

        #Iterates through all the course files
        for count, i in enumerate(class_file.readlines()):
            #Changes course path depending on index
            COURSE_PATH = "COURSE" + str(count + 1) + ".txt"
            course_file = open(COURSE_PATH, "r") #Opens course file
            course = [] #Array for all students in the course

            #Iterates through all student numbers
            for j in course_file.readlines():
                course.append(j.strip()) #Adds student numbers to the list

            course_file.close()
            
            classes.append(course) #Adds list to classes list
        class_file.close() 

        #Gets all students with names
        students_file = open(STUDENTS_PATH, "r")
        for i in students_file.readlines():
            students.append(i.strip().split(","))

    except FileNotFoundError:
        return False 
    return True

def makeCourse(n, classes, students):
    f = open("course" + str(n + 1) + ".html", "w")
    f.write("<html>")
    f.write("<h1>Course " + str(n+ 1) + " Examinees</h1>")
    f.write("<link rel = 'stylesheet' href = 'styles.css'")
    f.write("<body>")
    f.write("<table>")
    f.write("<tr>")
    f.write("<th>Student Number</th>")
    f.write("<th>Name</th>")
    f.write("</tr>")
    for i in classes[n]:
        f.write("<tr>")
        f.write("<td>" + i + "</td>" )
        f.write("<td>" + findName(i, students) + "</td>")
        f.write("</tr>")
     
    f.write("</table>")
    f.write("</body>")
    f.write("</html>")
    print("Created page for course " + str(n+1))
    
def findName(n, students):
    for i in students:
        if i[0] == n:
            return i[1]

#Creates html output
def output(color_index, classes, students):
    timestart = 8 #Sets at what time exams start

    f = open("index.html", "w")
    f.write("<html>")
    f.write("<h1>Exam schedules</h1>")
    f.write("<link rel = 'stylesheet' href = 'styles.css'")
    f.write("<body>")
    f.write("<table>")

    f.write("<tr>")
    f.write("<th>Exam time</th>")
    f.write("<th>Class/es</th>")
    f.write("</tr>")
    for i in range(max(color_index)):
        timeslot = []
        f.write("<tr>")
        f.write("<td>" + str(timestart + i) + ":00-" + str(timestart+ 1 + i) + ":00</td>")
        for j in range(len(classes)):
            if color_index[j] == i:
                timeslot.append("<a href = 'course" + str(j +1) + ".html'>COURSE" + str(j + 1) +"</a>")
        same_time = ", ".join(timeslot)
        f.write("<td>" + same_time + "</td>")
        f.write("</tr>")
    f.write("</table>")
    f.write("</body>")
    f.write("</html>")

    for i in range(len(classes)):
        makeCourse(i, classes, students)
    print("Successfully created index.html at current directory")


#Creates CSS output
def style():
    f = open('styles.css', 'w')
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
    print("Successfully created styles.css at current directory")



    
main()
