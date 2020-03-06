import re

# 数量词

#  解决输出完整的英文单词
a = 'python 777 java78yuyan###liuyue'
r = re.findall('[a-z]', a)
print(r)

r1 = re.findall('[a-z][a-z][a-z]', a)
print(r1)

r2 = re.findall('[a-z]{3}', a)
print(r2)

#  竟然能输出所有的英文字符串 而不是pyt三个
r3 = re.findall('[a-z]{3,6}', a)
print(r3)

