#列出一个数组 找到其中的最大值和最小值
l = [12,3,4,54,5,32,6,7,4,6,76]
n = len(l)
for i in range(0, n-1):
    for j in range(i, n):
        if l[i]<l[j]:
            l[i],l[j] = l[j],l[i]

print(l)
print(l[0])
print(l[n-1])

def findminanmax(l):
    if len(l) == 0:
        return (None, None)

    max = l[0]
    min = l[0]
    for i in l:
        if max > i:
            max = i
        elif min < i:
            min = i
    return max, min

print(findminanmax((1,2,4,5,2,76,)))
'''

def findMinAndMax(L):

    if(L==[]):

        return (None,None)

    max=L[0]

    min=L[0]

    for var in L[1:]:

        if var>max:

            max=var

        elif var<min:

            min=var

    return (min,max)

'''

def findMinAndMax(L):
    b = len(L)
    if(b==0):
        return(None,None)
    else:
        Max_num = Min_num  = L[0]
        for x in L:
            if(x <= Min_num):
                Min_num = x
            if(x >= Max_num):
                Max_num = x
        return (Min_num,Max_num)

print(findMinAndMax((1,3,4,5,6,6,3,4,5)))


