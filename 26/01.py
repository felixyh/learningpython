# 尝试编写一个用户登录程序（这次尝试将功能封装成函数），程序实现如图

log_user = {}

welcome_msg = '''
|---新建用户：N/n---|
|---登陆账号：E/e---|
|---退出程序：Q/q---|
'''

register_msg = '''
注册成功，赶紧试试登陆吧！
'''

logon_msg = '''
欢迎进入xxoo系统，请点击右上方的x结束程序！
'''

quit_msg = '''
已成功退出系统！
'''


def logon():
    name = input('请输入用户名：')
    while name not in log_user.keys():
        name = input('您输入的用户名不存在，请重新输入：')
    passwd = input('请输入密码：')
    count = 3
    while log_user[name] != passwd:
        count -= 1
        if count > 0:
            passwd = input('密码错误，请重新输入')
        else:
            print('密码输入错误3次，退出程序')
            break
    print(logon_msg)


def create():
    name = input('请输入用户名：')
    while name in log_user.keys():
        name = input('此用户已经被使用，请重新输入：')
    log_user.setdefault(name, input('请输入密码：'))
    print(register_msg)


def logon_main():
    while True:
        print(welcome_msg, end='')
        code = input('|---请输入指令代码：')

        if code == 'N' or code == 'n':
            create()
        elif code == 'E' or code == 'e':
            logon()
        elif code == 'Q' or code == 'q':
            print(quit_msg)
            break


if __name__ == '__main__':
    logon_main()




