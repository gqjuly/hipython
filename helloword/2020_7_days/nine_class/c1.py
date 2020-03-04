#面向对象
#有意义的面向对象的代码
#类 = 对象
#实例化
#类最基本的作用就是：封装
#类就是定义 刻画 描述一些东西 不能用来执行代码

#类和对象


class Student():  #括号可以放参数
    name = ''  #定义若干个变量
    age = 0

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

class StudentHomework():
    homework_name = ''

#方法 和 函数的区别 绝大多数没有区别
'''
方法：设计层面
函数： 程序运行、过程式的一种称谓
'''

# student = Student()
# student.print_file()