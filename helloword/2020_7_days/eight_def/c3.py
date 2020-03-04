'''
多结果返回函数方法
R Skill1 Skill2

'''

'''
两个知识点
1、返回多个值
2、返回值的类型不做要求 动态语言
3、用多个变量来接受返回值(元组的解剖方式用多个变量来接收 不用多个索引)
'''

# def damage(skill1, skill2):
#     damage1, damage2
#     return (damage1, damage2)
#
# def damage(skill1, skill2, out/ref damage):
#     damage1, damage2
#     return damage1

# def damage(skill1, skill2):
#     damage1 = skill1 * 3
#     damage2 = skill2 * 2 + 10
#     return damage1, damage2
#
# damages = damage(3, 6)
# print(damages)
# print(type(damages))
# print(damages[0])

def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2

skill1_damage, skill2_damage = damage(3, 6)

print(skill1_damage, skill2_damage)