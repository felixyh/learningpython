# 编写一个程序，实现“全部替换”功能，程序实现如图 ：

def file_replace(name, o_str, n_str):
    f_read = open(name, 'rt')
    f_content = f_read.read()
    f_read.close()
    count = f_content.count(o_str)
    if count == 0:
        print('没有找到需要替换的字符')
    else:
        print('文件 %s 中共有 %d 个 【%s】' %(name, count, o_str))
        print('你确定要把所有【%s】的替换为【%s】吗' %(o_str, n_str))
        answer = input('[YES/NO]:')
        if answer == 'YES':
            f_content = f_content.replace(o_str, n_str)
            f_write = open(name, 'w')
            f_write.write(f_content)
            f_write.close()


f_name = input('请输入文件名：')
old_str = input('请输入需要替换的单词或字符：')
new_str = input('请输入新的单词或字符：')


if __name__ == '__main__':
    file_replace(f_name, old_str, new_str)


