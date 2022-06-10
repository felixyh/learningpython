# 编写一个函数，分别统计传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其它字符的个数。


def count_str(var):
    str_count = 0
    space_count = 0
    number_count = 0
    other_count = 0

    for i in var:
        if i.isdigit():
            number_count += 1
        elif i.isalpha():
            str_count += 1
        elif i.isspace():
            space_count += 1
        else:
            other_count += 1

    print('英文字母个数是：%d' % str_count)
    print('数字个数是：%d' % number_count)
    print('空格个数是：%d' % space_count)
    print('其他字符个数是：%d' % other_count)


count_str('12d99  safe')

