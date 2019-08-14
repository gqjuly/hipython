#1-99的list
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n+1
print(L)

#比较切片
print([L[1], L[2], L[3]])
print(L[1:4])

#for ... in
r = []
n = 4
for i in range(n):
    r.append(L[i])

print(r)

#倒切片
print(L[-1:])
print(L[-2:-1])

#每多少个取数
#前面十个数 每两个取一个
print(L[:10:2])
#所有数字 每五个取一个数字
print(L[::5])

# ：代表0：0 就是所有list
print(L[:])

#字符串可以直接切片
A = 'ABCDEFG'
print(A[1:])
print(A[:1])
print(A[-1:])
print(A[:-1])

print(A[:3])
print(A[::2])

#练习题：
# 利用切片操作，实现一个trim()函数，
# 去除字符串首尾的空格，
# 注意不要调用str的strip()方法：

def trim(str):
    if str == ' ':
        return str
    elif str[:1]==' ':
        return str[1:]
    elif str[-1:]==' ':
        return  str[-1:]

print(trim(" abcdefg  ")+'ahahha')


def liu(str):
    if str == ' ':
        return str
    while str[:1] ==' ':
        str = str[1:]
    while str[-1:] == ' ':
        str = str[:-1]
    return str

print(liu(' abdcldl     ')+'ahahha')

def trimm(s):

    if s == '':

        return s

    while s[:1]==' ':

        s = s[1:]

    while s[-1:] == ' ':

        s = s[:-2]

    return s

print(trimm(" abcdefg     ")+'ahahha')



