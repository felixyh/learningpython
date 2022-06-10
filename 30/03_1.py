# 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图

import os
import os.path


def search_file(path, file_name):
    for folder, sub_folders, sub_files in os.walk(path):
        if file_name in sub_files:
            print(os.path.join(folder, file_name))


if __name__ == '__main__':
    search_file(input('请输入待查找的初始目录：'), input('请输入需要查找的目标文件：'))

