# WAP to implement Getters and Setters in a class.

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person("Aman")

print("Name:", p.get_name())

p.set_name("Ravi")
print("Updated Name:", p.get_name())