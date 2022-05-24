# 编写一个程序，计算当前文件夹下所有文件的大小，程序实现如图：

import os
import os.path


def file_size(f_path):
    os.chdir(f_path)
    file_list = list(filter(lambda x: os.path.isfile(x), os.listdir(f_path)))
    for each_file in file_list:
        print(each_file + '  【%d Bytes】 ' % os.path.getsize(each_file))


if __name__ == '__main__':
    file_size(input('please input the path:'))
