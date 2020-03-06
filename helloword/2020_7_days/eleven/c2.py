from enum import Enum

#枚举类
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
# print(VIP.BLACK)
# print(VIP.BLACK.value)
# print(VIP.BLACK.name)
# print(type(VIP.BLACK))
# print(type(VIP.BLACK.name))
# print(VIP['GREEN'])
for v in VIP:
    print(v)

#比较  等值可以 大小不可以比较
result = VIP.GREEN == VIP.BLACK
print(result)