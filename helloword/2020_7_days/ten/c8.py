import re
#  解决输出完整的英文单词


# 数量词
#  *  匹配0次或者无限多次
#  +  匹配1次或者无限多次
#  ?  匹配0次或者1次
a = 'pytho444pytho0python1pythonn2pythonnn7python'

r = re.findall('python*', a)
print(r)

r1 = re.findall('python+', a)
print(r1)

r2 = re.findall('python?', a)
print(r2)

r3 = re.findall('python{1}', a)
print(r3)

r4 = re.findall('python{1,3}', a)
print(r4)

r5 = re.findall('python{1,3}?', a)
print(r5)

r6 = re.findall('python', a)
print(r6)