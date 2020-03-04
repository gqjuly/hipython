class Student():
    sum = 0

    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age

    #定义类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

studend1 = Student('haha', 39)
studend2 = Student('hehe', 39)
studend3 = Student('大头', 39)
Student.plus_sum()