# WAP to calculate student grade using class.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

s1 = Student("Rahul", 82)

print("Name:", s1.name)
print("Marks:", s1.marks)
print("Grade:", s1.calculate_grade())