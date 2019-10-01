import random

class Thief:
    sneaky = True

    def pickpocket(self):
        if self.sneaky:
            return bool(random.randint(0,1))
        return False

brandon = Thief()

print(brandon.pickpocket())
print(Thief.pickpocket(brandon))

class Student:
    def praise(self):
        name = "Brandon"
        return print("You're doing a great job {}".format(name))

student = Student()

print(student.praise())



