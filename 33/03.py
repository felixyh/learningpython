# 尝试一个新的函数 int_input()，当用户输入整数的时候正常返回，否则提示出错并要求重新输入

def int_input(msg=''):
    flag = True
    try:
        number = input(msg)
        temp = int(number)
    except ValueError as reason:
        print('输入类型出错啦@ \n出错类型： %s' % str(reason))
        flag = False
    while flag:
        if isinstance(temp, int):
            return temp
            break
        else:
            temp = input('error captured, please input again\n')


print(int_input())

