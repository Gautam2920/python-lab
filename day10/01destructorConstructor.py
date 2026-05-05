# WAP to implement destructor and constructors using _del() and __init_().

class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called. Student name:", self.name)

    def __del__(self):
        print("Destructor called. Object deleted")

s1 = Student("Rahul")

del s1