# import hello
# import package.test as yUnresolved reference 'package'
# print(hello.a)
# print(package.test.a)
# print(y.b)

# from hello import a
# print(a)

# from package import test
# print(test.a)

from package.test import *

print(a)
# print(b)
print(c)

