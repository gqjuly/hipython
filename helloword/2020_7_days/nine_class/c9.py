class Human():
    my_sum = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('father english homework')

# people = Human('haha', 20)
# people.get_name()