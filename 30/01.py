# 编写一个程序，统计当前目录下每个文件类型的文件数，程序实现如图：
import os
import os.path


def count_ext(file_path):
    ext_dic = {}
    count = 0
    dir_elements = os.listdir(file_path)
    for each in dir_elements:
        ext = os.path.splitext(each)[1]
        if ext not in ext_dic.keys():
            ext_dic.setdefault(ext, 1)
        else:
            ext_dic[ext] += 1
    for each_ext in ext_dic.keys():
        if each_ext =='':
            print('文件夹：【 %s 】下共有类型为文件夹的文件 %d 个' % (file_path, ext_dic[each_ext]))
        else:
            print('文件夹：【 %s 】下共有类型为 [ %s ] 的文件 %d 个' % (file_path, each_ext, ext_dic[each_ext]))


count_ext(os.path.curdir)
