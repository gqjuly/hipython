# 对于任意一个序列 打印1357.。。
a = [1, 2, 3, 4, 5, 6, 7, 8]

#自己答案1
# for x in a:
#     if x % 2 != 0:
#         print(x)

#自己答案2
# for x in range(1, 8, 2):
#     print(x)

#标准答案 利用for循环
for i in range(0, len(a), 2):
    print(a[i], end=" | ")

#标准答案 利用切片
b = a[0:len(a):2]
print(b)