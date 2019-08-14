#列表排序（选择法）
l = [0, 9, 8, 5, 4, 6, 3, 6, 6, 2]

n = len(l)

for i in range(0,n-1):
    for j in range(i, n-1):
        if l[i]<l[j]:
            l[i],l[j] = l[j],l[i]
print(l)


#从终端输入两个整数m，n，打印m*n的表格，如：2,5，打印如下效果
#1 2 3 4 5
#6 7 8 9 10
m=int(input('请输入一个整数：'));
n= int(input('请输入第二个整数'));
i =1
while i < m*n+1:

    print(i)
    i=i + 1

m = int(input("请输入一个数字"))
n = int(input("请输入一个数字"))

for x in range(1,m+1):
   for y in range(1,n+1):
       print("{}".format((x-1)*n+y),end="    ")
   print()




