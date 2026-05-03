class Book:
    def __init__(self, book_id, name):
        self.book_id = book_id
        self.name = name
        self.issued = False

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.books = []

class Library:
    def __init__(self):
        self.books = {}
        self.students = {}

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        self.students[student_id] = Student(student_id, name)
        print("Student added successfully!\n")

    def issue_book(self):
        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID: ")
        
        if student_id in self.students and book_id in self.books:
            if not self.books[book_id].issued:
                self.books[book_id].issued = True
                self.students[student_id].books.append(book_id)
                print("Book issued successfully!\n")
            else:
                print("Book is already issued!\n")
        else:
            print("Student or Book not found!\n")

    def return_book(self):
        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID: ")
        
        if student_id in self.students and book_id in self.books:
            if book_id in self.students[student_id].books:
                self.books[book_id].issued = False
                self.students[student_id].books.remove(book_id)
                print("Book returned successfully!\n")
            else:
                print("This book was not issued to this student!\n")
        else:
            print("Student or Book not found!\n")

    def show_books(self):
        print("\n=== Library Books ===")
        for book in self.books.values():
            status = "Issued" if book.issued else "Available"
            print(f"{book.book_id} | {book.name} | {status}")



lib = Library()


lib.books["B001"] = Book("B001", "Python Basics by W3 School")
lib.books["B002"] = Book("B002", "Poetry Book by Allama Iqbal")
lib.books["B003"] = Book("B003", "Math Book")
lib.books["B004"] = Book("B004", "Harry Potter Novel")
lib.books["B005"] = Book("B004", "Pakistan History")
lib.books["B006"] = Book("B004", "william shikspear novel")
lib.books["B007"] = Book("B004", "AI books")




while True:
    print("\n  LIBRARY MANAGMENT SYSTEM")
    print("1. Add Student")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show Books")
    print("5. Exit")
    
    ch = input("\nChoose option (1-5): ")
    
    if ch == "1":
        lib.add_student()
    elif ch == "2":
        lib.issue_book()
    elif ch == "3":
        lib.return_book()
    elif ch == "4":
        lib.show_books()
    elif ch == "5":
        print("Thank you! Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")