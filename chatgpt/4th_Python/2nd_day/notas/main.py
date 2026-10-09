from models.student import Student

student1 = Student("Lucas", 8.0, 9.0)
student2 = Student("Emily", 6.0, 5.0)
student3 = Student("Robert", 3.0, 4.0)

students = [student1, student2, student3]

for student in students:
    student.display_report()
    print("-" * 30)