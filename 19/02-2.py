# 编写一个函数，分别统计传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其它字符的个数。

# 多个参数的情况

def count_str(*param):
    var_number = len(param)
    for i in range(var_number):
        str_count = 0
        space_count = 0
        number_count = 0
        other_count = 0
        for each in param[i]:
            if each.isdigit():
                number_count += 1
            elif each.isalpha():
                str_count += 1
            elif each.isspace():
                space_count += 1
            else:
                other_count += 1
        print('第 %d 个参数有 %d 英文字母，%d 数字， %d 空格， %d 其他字符' % (i, str_count, number_count, space_count, other_count))


count_str('1fe', '1ssssf sfe')

