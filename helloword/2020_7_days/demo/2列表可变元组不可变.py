a = [1, 2, 3]
print(id(a))
print(hex(id(a)))

a[0] = "1"
print(id(a))

a = (1, 2, 3)
#a[0] = "1" #报错

b = [1, 2, 3]
b.append(4)
print(b)

c = (1, 2, 3)
#c.append(4)  #报错


#多维元组
a = (1, 2, 3, [1, 2, 4])
print(a[3][2])
a[3].append(5)
print(a)