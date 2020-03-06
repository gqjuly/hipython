
import re
#概括字符集

#  \d \D 匹配0-9的数字 和 非数字
a = 'C3C++4Java5C#4Python1Java&Script \n'
r = re.findall('\d', a)
print(r)

#  用0-9 也可以表达 或者^0-9表达
r = re.findall('[^0-9]', a)
print(r)

#  \w  匹配所有的字符集
#匹配不到&  只能匹配单词字符
# 匹配到的内容[A-Za-z0-9_]
w = re.findall('\w', a)
w1 = re.findall('[A-Za-z0-9_]', a)
print(w)
print(w1)

#\W 匹配所有的非字符集
w3 = re.findall('\W', a)
print(w3)

#\s 空白字符  \S非空白字符
s = re.findall('\s', a)
print(s)



