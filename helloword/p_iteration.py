#例子
d ={'a':1 , 'b':2, 'c':3}
for key in d:
    print(key)



for ch in 'ABC':
    print(ch)

#for in
#遍历字符串
s = 'i love you more than i can say'
for x in s:
    print(x)
#遍历列表
l = ['我爱你', '高秋佳', '你知道吗']
for y in l:
    print(l)

for i, v in enumerate(l):
    print(i, v)

#遍历字典
d = {'a': 'apple', 'b': 'banana', 'c':'car', 'd':'desk'}
for key in d:
    print(key, d.get(key))
#第二种 d.item() = dict.items(d)
for key2, value in dict.items(d):
    print(key2, value)


#如何判断一个对象是否是可迭代对象
from collections import Iterable
print(isinstance(123, Iterable))

#可以迭代的对象
print(range(10))
print(range(0,10))

for i in range(10):
    print(i)
#强制转换为列表
print(list(range(1,11)))

#列表生成式
print([i for i in range(1, 11)])
print([i*2 for i in range(1, 11)])
print([i*i for i in range(1, 11)])
print([str(i) for i in range(1, 11)])
print([i for i in range(1, 11) if i%2 ==0])

#例子
#输入一个整数 出下列图形
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ...
# 1 2 3 4 ... n
n = int(input('请输入一个整数'));
j = 1
while j<=n:
    i = 1
    while i <=j:
        print(i, end=' ')
        i = i + 1
    print()
    j = j+1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

#九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(j,'*',i,'=',i*j, end=' ')
    print()

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}'.format(j, i, j*i), end=' ')
    print()


