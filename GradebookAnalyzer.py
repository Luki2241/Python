#declares variables and functions
options = [1, 2, 3, 4, 5]
optionuser = ""
students = {}
name = ""
grade = 0
searchstudent = ""

def add_student():
    name = input("Enter the students name: ").capitalize()
    if name in students:
        print("Student already exists.")
    else:
        students[name] = None
        print("Student added.")    
    
def add_studentgrade():
    #prints students grade
    print("Students:", list(students.keys()))
    if len(students) > 0:
        searchstudent = input("Which student do you wanna give a grade?: ").capitalize()
        if searchstudent in students:
                grade = int(input("Enter the students grade (in numbers): "))
                students[searchstudent] = grade
                print("Grade added.")
        else:
            print("No student found.")
    else:
        print("No student found.")    
    
def calcavgclass(): 
    #counts all graded students with a list comprehension
    graded_students = [g for g in students.values() if g is not None]
    
    if len(students) == 0:
        print("No student is graded.")
    else: 
        avg = sum(graded_students) / len(graded_students)
        print("The average grade is:", avg)
        
def viewstudents():
    if len(students) > 0:
        for name, grade in students.items():
            print(name, ":", grade)
    else:
        print("There  are no students.")
        
while True:
    print("1. Add student")
    print()
    print("2. Add student's grade")
    print()
    print("3. Calculate class average")
    print()
    print("4. View Students and grades")
    print()
    print("5. Exit")
    optionuser = int(input("Choose an option: "))

    if optionuser == options[0]:
        add_student()
        
    elif optionuser == options[1]:
        add_studentgrade()
        
    elif optionuser == options[2]:
        calcavgclass()
        
    elif optionuser == options[3]:
        viewstudents()
        
    elif optionuser == options[4]:
        print("Quitting...")
        quit()
        
    else:
        print("Invalid option.")