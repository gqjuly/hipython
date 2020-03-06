import re
lanuage = 'PythonC#/nJavaPHPC#LLLC#'
#.sub替换
#五个参数  查找的 替换的 字符串 替换次数


#.sub深入使用方法
def convert(value):
    t = value.group()
    print('||' + t + '||')
r = re.sub('C#', convert, lanuage, 1)
print(r)

