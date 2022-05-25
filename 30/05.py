# 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），
# 要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），程序实现如图

import os
import os.path


def search_keyword(path, keyword):
    for folder, sub_folders, sub_files in os.walk(path):
        for each_file in sub_files:
            f_open = open(each_file, 'rt')
            if keyword in f_open.readline():

        if file_name in sub_files:
            print(os.path.join(folder, file_name))