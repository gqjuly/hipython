#默认情况下，dict迭代的是key
#如果要迭代value，可以用for value in d.values()
#如果要同时迭代key和value，可以用for k, v in d.items()
d = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

#显示dict中的key
for key in d:
    print(key)

for value in d:
    print(value)

#显示dict中的value
for value in d.values():
    print(value)

#依次显示dict中的item
for k,v in d.items():
    print(k,v)


#由于字符串也是可迭代对象，因此，也可以作用于for循环
for str in 'ABCDEFG':
    print(str)

#判断是否可以迭代
#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
isinstance('abc', Iterable)

isinstance(123, Iterable) # str是否可迭代

#最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码
for x, y in [(1,2) , (2,4), (4,8)]:
    print(x, y)


#作业：请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(l):
    if len(l)==0:
        return (None, None)
    max = l[0]
    min = l[0]
    for i in l:
        if max < i:
            max = i
        if min > i:
            min = i
    return (min, max)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')