'''
类是现实世界或四维世界中的实体在计算中的反映
他将数据以及这些数据上的操作封装在一起
'''

class Student():
    name = ''
    age = 0
    #特殊函数
    #类变量 实例变量
    def __init__(self, name, age):
        #构造函数
        #初始化对象的属性
        self.name = name
        self.age = age

    def do_homework(self):
        print('homework')

student1 = Student('大头', 89)
print(student1.name)
print(student1.age)