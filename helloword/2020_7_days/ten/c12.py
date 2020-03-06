import re
s = 'life is short, i use python'
#提取life 和 pyhton之间的数据

# r = re.search('life.*python', s)
# print(r.group())
# print(r.group(0))

r = re.search('life(.*)python', s)
print(r.group())
print(r.group(0))
print(r.group(1))
print(r.group(0,1))
print(r.groups())
