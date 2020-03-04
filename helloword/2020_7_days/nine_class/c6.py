
class Student():

    name = '小头'
    age = 0

    def __init__(self, name, age):
        #构造函数
        #初始化对象的属性
        self.name = name
        self.age = age

        print(self.name)
        print(name)
        #经典错误 name等于self.name 这个name找到的是形式参数name



student1 = Student('大头', 89)
