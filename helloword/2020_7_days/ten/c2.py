
import re
#判断字符串中是否有Python
a = 'C|C++|Java|C#|Python|JavaScript'

r = re.findall('Python', a)
if len(r) != 0:
    print('字符串中包含Python')
else:
    print('NO')
# print(r)


#方法一
var = a.index('Python') > -1
print(var)

#方法二
print('Python' in a)

