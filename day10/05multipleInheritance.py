# WAP to illustrate multiple inheritance in Python.

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skills(self):
        print("Child inherits both skills")

c = Child()
c.skill1()
c.skill2()
c.skills()