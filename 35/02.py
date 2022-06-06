# 实现一个用于登记用户账号信息的界面（如果是带*号的必填项，要求一定要有输入并且不能是空格）

import easygui as g
import sys


message = "【真实姓名】为必填项 \n【手机号码】为必填项 \n【*E-mail地址】为必填项 "
title = "账号中心"
fields = ['*用户名', '*真实姓名', '固定电话', '*手机号码',  'QQ', '*E-mail']
result = g.multenterbox(msg=message, title=title, fields=fields, values=['小甲鱼'], callback=None, run=True)
while True:
    if not result:
        sys.exit()
    elif result[1].isspace() or not result[1]:
        g.msgbox('【真实姓名】为必填项, 一定要有输入并且不能是空格')
    elif result[3].isspace() or not result[3]:
        g.msgbox('【手机号码】为必填项, 一定要有输入并且不能是空格')
    elif result[5].isspace() or not result[5]:
        g.msgbox('【E-mail】为必填项, 一定要有输入并且不能是空格')
    else:
        break
    result = g.multenterbox(msg=message, title=title, fields=fields, values=['小甲鱼'], callback=None, run=True)

g.msgbox('登记成功@！')





