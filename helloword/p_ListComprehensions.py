#List comprehensions
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

#生成1-10的列表
l = list(range(1,11))
print(l)

#生成1*1 2*2~10*10的列表

#方法一 循环
L= []
for x in range(1,11):
    L.append(x*x)
print(L)

#方法二
L = [x * x for x in range(1,11)]
print(L)

#筛选
L = [x * x for x in range(1,11) if x % 2 ==0]
print(L)

#拓展 字符串ABC和QWE的集合
Y = [x + y for x in 'ABC' for y in 'QWE']
print(Y)

#列出所有文件夹名称
import os
l = [d for d in os.listdir('.')]
print(l)

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {
    'a': '23',
    'b': '24',
    'c': '25'
}
for i, j in d.items():
    print(i,'=',j)

#two
l = []
l = [x + '=' + y for x, y in d.items()]
print(l)


#把一个list中所有的字符串变成小写
l = ['Hello', 'Python', 'Hahahaha', 'Heiheiehie']
L = [s.lower() for s in l]
print(L)

#作业
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
#
L1= ['Hello', 'World', 18, 'Apple', None]
L2 =[]
for y in L1:
    if isinstance(y , str):
        L2.append(y.lower())

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#list comprehensions
L2 = [ i.lower() for i in L1 if isinstance(i , str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')