'''
类是现实世界或四维世界中的实体在计算中的反映
他将数据以及这些数据上的操作封装在一起
'''

class Student():
    name = ''
    age = 0
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