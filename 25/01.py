# 尝试利用字典的特性编写一个通讯录程序吧


address_book = {'小甲鱼': '020-88974563', 'Felix': '025-52680000'}
welcome_msg = '''
|--- 欢迎进入通讯录程序---|
|--- 1： 查询联系人资料---|
|--- 2： 插入新的联系人---|
|--- 3： 删除已有联系人---|
|--- 4： 退出通讯录程序---|
'''
bye_msg = '''
|--- 感谢使用通讯录程序---|
'''


def ad_search():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        print(address_book[name])
    else:
        print('输入的联系人不存在！')


def ad_insert():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        print('您输入的姓名在通讯录中已存在 --->> %s : %s' %(name, address_book[name]))
        edit_check = input('是否修改用户资料（YES/NO）')
        if edit_check == 'YES':
            address_book[name] = input('请输入用户联系电话：')
    else:
        phone = input('请输入用户联系电话：')
        address_book[name] = phone


def ad_delete():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        del_check = input('是否删除已有联系人: %s（YES/NO）' % name)
        if del_check == 'YES':
            del address_book[name]
    else:
        print('输入的联系人不存在！')


def address():
    while True:
        print(welcome_msg)
        code = int(input('请输入相关的指令代码：'))
        if code == 2:
            ad_insert()
        elif code == 1:
            ad_search()
        elif code == 3:
            ad_delete()
        elif code == 4:
            print(bye_msg)
            break
        else:
            print('输入有误，请重新输入代码')


if __name__ == '__main__':
    address()
