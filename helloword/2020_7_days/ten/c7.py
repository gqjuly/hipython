import re

# 数量词

#  解决输出完整的英文单词
a = 'python 777 java78yuyan###liuyue'

#  竟然能输出所有的英文字符串
#  贪婪与非贪婪
r3 = re.findall('[a-z]{3,6}', a)
print(r3)

r3 = re.findall('[a-z]{3,6}?', a)
print(r3)