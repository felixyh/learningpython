import re  # 导入re模块


def fn():
    f = open('string2.txt', 'r')
    a = f.read()
    l = re.findall('[^A-Z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]{1}',a)
    '''选出符合题目要求的字母区间。中间为小写字母，密码的左右两边均有且只有三个大
    写字母（说明两边三个大写字母之后只要是非大写字母的即满足条件）,此时返回的是一个列表'''
    for i in l:  # 遍历列表
        print(i[4], end=' ')  # 打印第四个字母


fn()
