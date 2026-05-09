student = {}

while True:
    print("=======STUDENT RESULT MANAGER=======")
    print("1.Add student")
    print("2.View students")
    print("3.Check result")
    print("4.Exit")

    choice = input("Enter your choice: ")    

# Add Student
    if choice =="1":
        name= input("Enter Student Name:")
        marks= int(input("Enter Student Marks: "))
        student[name] = marks
        print(f"{name} Successfully Added!")

# View Student
    elif choice == "2":
        if not student:
          print("Student not found")
        else:
          for name, marks in student.items():
            print(name , ":" , marks)    

# Check Result

    elif choice == "3":
        name = input("Enter Student Name:")

        if name in student:
            marks = student[name]
            if marks >= 40:
              print("PASS")
            else:
              print("FAIL")     
        else:
          print("Student Not Found!")

# Exit

    elif choice == "4":
        print("System: Terminating process...")
        break

    else:
        print("Invalid Selection: Please verify your input and try again.")