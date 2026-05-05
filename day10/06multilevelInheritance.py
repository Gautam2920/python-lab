# WAP to illustrate multilevel inheritance in Python.

class Grandparent:
    def gp_method(self):
        print("Grandparent class")

class Parent(Grandparent):
    def p_method(self):
        print("Parent class")

class Child(Parent):
    def c_method(self):
        print("Child class")

c = Child()
c.gp_method()
c.p_method()
c.c_method()