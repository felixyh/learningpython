# 呃，不得不说我们的用户变得越来越刁钻了。
# 要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
# （如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）


def show_file(name, rows):
    f_open = open(name, 'rt')
    f_lines = f_open.readlines()

    start_s, end_s = rows.split(':')
    if start_s == '':
        row_start = 0
        row_start_msg = '开始'
    else:
        row_start = int(start_s)-1
        row_start_msg = '第' + start_s + '行'
    if end_s == '':
        row_end = len(f_lines)
        row_end_msg = '末尾'
    else:
        row_end = int(end_s)
        row_end_msg = '第' + end_s + '行'

    print('文件 %s 从 %s 到 %s 行的内容如下：' % (f_name, row_start_msg, row_end_msg))
    for each_line in range(row_start, row_end):
        print(f_lines[each_line], end='')
    f_open.close()


f_name = input('请输入要打开的文件：')
f_rows = input('请输入需要显示的行数【格式如 13：21 或 ：21 或 21：】：')


if __name__ == '__main__':
    show_file(f_name, f_rows)

