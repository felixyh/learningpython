# 1. 请写一个密码安全性检查的脚本代码：check.py
#
# 密码安全性检查代码
#
# 低级密码要求：
#
# 1. 密码由单纯的数字或字母组成
# 2. 密码长度小于等于8位
#
# 中级密码要求：
#
# 1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合 *
# 2. 密码长度不能低于8位
#
# 高级密码要求：
#
# 1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
# 2. 密码只能由字母开头
# 3. 密码长度不能低于16位

specialchar = '''~!@#$%^&*()_=-/,.?<>;:[]{}|\\'''

while True:
    alphaflag, digitflag, specharflag = 0, 0, 0
    passstr = input('Please input your password: ')

    for each in passstr:
        if each.isalpha():
            alphaflag = 1
        elif each.isdigit():
            digitflag = 1
        elif each in specialchar:
            specharflag = 1
        else:
            continue

    passlen = len(passstr)

    if passstr[0].isalpha() and passlen >= 16 and alphaflag+digitflag+specharflag == 3:
        print('The password is strong!')
        break
    elif passlen >= 8 and alphaflag+digitflag+specharflag >= 2:
        print('The password is medium!')
        break
    elif passlen < 8 and (passstr.isdigit() or passstr.isalpha()):
        print('The password is weak!')
        break
    else:
        print('The password does not meet requirement, please input again!')
