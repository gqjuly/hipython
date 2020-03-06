import json

#JSON  object array
json_str = '[{"name":"qiyue", "age":18, "flag" : false}, {"name":"qiyue", "age":18}]'

#用python内置方法操作json字符串

student = json.loads(json_str)
print(student)
print(type(json_str))
print(type(student))
# print(student['name'])
# print(student['age'])