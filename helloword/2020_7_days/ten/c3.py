import re

# 把a中所有的数字索取出来
a = 'C3C++4Java5C#4Python1JavaScript'
x = re.findall('3', a)
print(x)

b = re.findall('\d', a)
print(b)

c = re.findall('\D', a)
print(c)

"""
'python' 普通字符
'\d' 元字符
"""
