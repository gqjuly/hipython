

class Student():
    name = '小头'
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student('大头', 89)
print(student1.name)
print(student1.age)
print(student1.__dict__)
print(Student.__dict__)