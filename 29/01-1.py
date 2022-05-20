# 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图

name = input('请输入文件名：')
f = open(name, 'x')
print('请输入内容【单独输入\':w\' 保存退出】:')

# 用内置函数iter实现等待输入， 让input()遇到回车键也能持续输入
txt = ''
for line in iter(input, ':w'):
    txt += line + '\n'


f.write(txt)
f.close()