# Practice

number = input('请输入一个整数（输入Q结束程序）：')

while True:
    if number == 'Q':
        print('程序结束')
        break
    elif number.isdigit():
        intnumber = int(number)
        print('{0}{1:#x}'.format('十进制 -> 十六进制：', intnumber))
        print('{0}{1:#o}'.format('十进制 -> 八进制：', intnumber))
        print('{0}{1:#b}'.format('十进制 -> 二进制：', intnumber))
        break
    else:
        number = input('输入错误，请重新输入一个整数（输入Q结束程序）：')
        continue

