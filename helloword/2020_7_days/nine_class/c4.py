'''
类是现实世界或四维世界中的实体在计算中的反映
他将数据以及这些数据上的操作封装在一起
'''

class Student():
    name = ''
    age = 0
    #特殊函数
    def __init__(self, name, age):
        #构造函数
        #初始化对象的属性
        name = name
        age = age
        print('student')

    def do_homework(self):
        print('homework')
'''
行为和特征
'''

 #打印应该重新添加一个打印类 行为和主体要放在一起
# class Printer():
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))

'''
类相当于一个模板一样 可以用一个模板产生很多个对象
学生的属性名字是个模板，具体的名字性别实例化之后就是对象了
'''

# student1 = Student()
# student2 = Student()
# student3 = Student()
# print(id(student1))
# print(id(student2))
# print(id(student3))
#三个实例化的对象的id完全不一样

'''
使三个对象实例化的对象不相同
1、在class里面定义一个特殊的函数
'''

# student1 = Student()
# a = student1.__init__()
# print(a)
# print(type(a))
#构造函数返回None 不能返回其他值

student1 = Student('大头', 89)
print(student1.name)