def read(classes, student_nos, student_names):
    CLASSES_PATH = "../input/classes.txt"

    class_file = open(CLASSES_PATH, "r")
    classes = [class_file.readline().strip() for i in class_file]

def main():
    classes = []
    student_nos = []
    student_names = []
    read(classes, student_nos, student_names)
    
main()
