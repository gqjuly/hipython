import json

student = [
    {'name': 'qiyue', 'age': 18, 'flag': False},
    {'name': 'liuyue', 'age': 48}
]

json_str = json.dumps(student)
print(json_str)
print(type(json_str))

"""
JSON对象 JSON JSON字符串
JSON对象：放在JavaScript中存在 放在python没有这个说法

"""

