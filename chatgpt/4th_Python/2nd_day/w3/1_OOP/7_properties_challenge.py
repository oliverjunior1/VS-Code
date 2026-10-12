# Create a class Student with an __init__ that takes name and grade, and stores them as properties
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Create an object s1 with name "Anna" and grade "A"
s1 = Student("Anna", "A")

# Print the grade of s1
print(s1.grade)

# Change the grade of s1 to "B"
s1.grade = "B"

# Print the updated grade
print(s1.grade)