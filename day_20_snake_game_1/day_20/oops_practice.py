# class Student:
#     name = "kashish upadhyay"
#
# s1 = Student()
# print(s1.name)

class Student:
    name = ""
    def __init__(self, name):
        self.name = name

s1 = Student("kashish")
print(s1.name)