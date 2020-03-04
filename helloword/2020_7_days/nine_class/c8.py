
from c9 import Human
"""
继承性：
避免我们定义重复的方法和变量
"""

class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self,name, age)
        super(Student, self).__init__(name, age)
    #     self.__sorce = 0

    def do_homework(self):
        super(Student, self).do_homework()
        print('english homework')


"""
变量都是可以继承的
"""
# student1 = Student('刘越', 68)
# print(student1.my_sum)
# print(Student.my_sum)
# print(student1.name)
# print(Student.name)

student1 = Student('人民路小学', '刘越', 68)
print(student1.school)

student1.do_homework()






