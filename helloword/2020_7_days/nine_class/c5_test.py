

class Student():

    sum = 0
    name = '小头'
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        while self.sum < 1000:
            self.sum += 1
        print(name)
        print(age)
        print(self.sum)
        print(Student.sum)


student1 = Student('大头', 89)
