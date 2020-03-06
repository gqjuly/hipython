#字符集
import re
s = 'abc, acc, adc, aec, afc, ahc, ahh, acd, aci'
#找出ac中间字符 为c 或者 为f 的字符串
# r = re.findall('a[cf]c', s)
# print(r)

#找出ac中间字符 不 为c 或者 为f 的字符串
# r = re.findall('a[^cf]c', s)
# print(r)

#找出ac中间字符 为c 到 为f 的字符串
r = re.findall('a[c-f]c', s)
print(r)