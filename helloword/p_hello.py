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