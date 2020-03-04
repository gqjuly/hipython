def print_studend_files(name, gender='男', age='18', college='宜春学院'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')


print_studend_files('鸡小萌', '男', 18, '人民路小学')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_studend_files('刘大越')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_studend_files('gaoqiujia', '女', '16')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_studend_files('hahah', age = '99')