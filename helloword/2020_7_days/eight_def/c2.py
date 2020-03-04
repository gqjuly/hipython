'''
1、参数列表可以没有
2、return value None
'''

#例子
'''
1、实现两个数字的相加
2、打印输入的参数
'''


def add(x, y):
    result = x + y
    return result

def pri(code):
    print(code)

a = add(1, 2)
b = pri('Python')

print(a, b)
#pri()函数里面没有return 所以返回的值为None
