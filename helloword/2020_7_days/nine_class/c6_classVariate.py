class Student():
    sum = 0

    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age

    def printerSum(self):
        self.__class__.sum += 1
        print('班级人数总数：' + str(self.__class__.sum))


student1 = Student('大头', 89)
student1.printerSum()
student2 = Student('er头', 80)
student2.printerSum()
student3 = Student('there头', 62)
student3.printerSum()
