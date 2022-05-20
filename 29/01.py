# 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图


name = input('请输入文件名：')
# lines = []
f = open(name, 'x')
print('请输入内容【单独输入\':w\' 保存退出】:')


while True:
    # 其实是循环等待每行输入，但是让input的输入提示符为空，效果是看起来一直没有打断的输入
    content = input()
    if content != ':w':
        content += '\n'
        f.write(content)
    else:
        break
        f.close()


