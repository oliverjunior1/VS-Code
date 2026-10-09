class Student:
    def __init__(self, name, grade1, grade2):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2

    def calculate_average(self):
        return (self.grade1 + self.grade2)/2

    def check_status(self):
        average = self.calculate_average()

        if average >= 7:
            return "Passed"
        elif average >= 5:
            return "Remedial"
        else:
            return "Failded"

    def display_report(self):
        print(f"Student: {self.name}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Status: {self.check_status()}")