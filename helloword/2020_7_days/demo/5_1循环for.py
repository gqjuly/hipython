#for

# for  主要是用来遍历/循环 序列或者集合、字典
# a = ['apple', 'orange', 'banana', 'grape']
#
# for x in a:
#     print(x)
#

#for 和else  else很少用
# a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
#
# for x in a:
#     for y in x:
#         print(y, end=' ')
# else:
#     print('fruit is gone')

#break
# a = [1, 2, 3]
# for x in a:
#     if x == 2:
#         break
#     print(x)

#continue
# a = [1, 2, 3]
# for x in a:
#     if x == 2:
#         continue
#     print(x)

#break 加else
# a = [1, 2, 3]
# for x in a:
#     if x == 2:
#         break
#     print(x)
# else:
#     print("EOF")

#continue 加else
# a = [1, 2, 3]
# for x in a:
#     if x == 2:
#         continue
#     print(x)
# else:
#     print('EOF')

#for 和else  else很少用
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]

for x in a:
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('fruit is gone')