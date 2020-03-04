class Student():
    sum = 0
    name = '小头'
    age = 18

    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age
        self.__sorce = 0

    # 定义类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        print(cls.name)

    # 定义静态方法
    @staticmethod
    def add(x, y):
        print(Student.sum)
        print('This is staticMethod')

    def __making(self, sorce):
        self.__sorce = sorce
        print(self.sorce)


# studend1 = Student('haha', 39)
# studend2 = Student('hehe', 39)
studend3 = Student('大头', 39)
Student.plus_sum()  # 类调用类方法
studend3.plus_sum()  # 对象调用类方法
Student.add(1, 2)  # 类调用静态方法
studend3.add(1, 2)  # 对象调用方法
studend3.__making(50)
studend3.__sorce = -1
print(studend3.__sorce)
