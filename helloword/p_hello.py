print("hello , pycharm")
print("hello, word")



#递归例子
def fact(n):
    if n == 1:
        return  1
    return  n*fact(n-1)
print(fact(5))

#尾递归优化
def factha(n):
    return facthaha(n , 1)
def facthaha(num , b):
    if num == 1:
        return b
    return facthaha(num-1 , num*b)

print(factha(5))


def liu(y):
    if y == 1:
        return 1
    return y*liu(y-1)
print(liu(5))

#作业 打印list中的元素
L =[
    ["haha", "hehe", "heihei"],
    ["六月", "七月", "八月"],
    ["黄色", "红色", "紫色"]
]

#打印hehe
print(L[0][1])