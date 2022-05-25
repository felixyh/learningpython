# 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图

import os
import os.path


def search_file(path, file_name):
    os.chdir(path)
    temp_folder_name = list(filter(lambda x: os.path.isdir(x), os.listdir(path)))
    temp_file_name = list(filter(lambda x: os.path.isfile(x), os.listdir(path)))
    if file_name in temp_file_name:
        print(os.path.join(path, file_name))
    if temp_folder_name:
        for sub_folder_name in temp_folder_name:
            search_file(os.path.join(path, sub_folder_name), file_name)


if __name__ == '__main__':
    search_file(input('请输入待查找的初始目录：'), input('请输入需要查找的目标文件：'))
