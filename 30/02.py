# 编写一个程序，计算当前文件夹下所有文件的大小，程序实现如图：

import os
import os.path


def file_size(f_path):
    for each_file in os.path.join(f_path, os.listdir(f_path)):
        if os.path.isfile(each_file):
            print(each_file + '[ %d Bytes ] ' % os.path.getsize(each_file))

    print(f_path)
    print(os.path.join(f_path, os.listdir(f_path)))


file_size('/Users/felix/PycharmProjects/learningpython')
