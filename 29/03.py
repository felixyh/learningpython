# 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，程序实现如图：

def show_file(name, rows):
    f_open = open(name, 'rt')
    for i in range(int(rows)):
        print(f_open.readline(), end='')
    f_open.close()


f_name = input('请输入要打开的文件：')
f_rows = input('请输入需要显示该文件前几行：')
print('文件 %s 的前 %s 的内容如下：' % (f_name, f_rows))

if __name__ == '__main__':
    show_file(f_name, f_rows)
