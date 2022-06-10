def int_input(prompt=''):
    while True:
        try:
            int(input(prompt))
            break
        except ValueError:
            print('出错，您输入的不是整数！')


int_input('请输入一个整数：')