import re
'''
re.match
re.search
返回结果是对象
搜索成功 立即停止
'''

s = 'a423435cdfdsk323kdjfd'

r = re.match('\d', s)
print(r)

r1 = re.search('\d', s)
print(r1)
print(r1.group())
print(r1.span())

r2 = re.findall('\d', s)
print(r2)