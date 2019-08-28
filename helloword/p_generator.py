#generator
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
l = [x * x for x in range(10)]
print(l)
g = (x * x for x in range(10))
print(g)

#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

#我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print(next(g))

print(next(g))

L =[]
for n in g:
    L.append(n)
print(L)

#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
#输出斐波那契的前max位
def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return "done"
print(fib(6))

#把上面的列子变成生成器 generator
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字
# 那么这个函数就不再是一个普通函数，而是一个generator
def fib2(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return "done"


for n in fib2(6):
    print(n)

#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
#例子
def odd():
    print('step1')
    yield (1)
    print('step2')
    yield (2)
    print('step3')
    yield (3)
o = odd()
print(o)
next(odd())
next(o)
next(o)
