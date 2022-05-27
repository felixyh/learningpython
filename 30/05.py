# 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），
# 要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），程序实现如图

import os
import os.path


# 存放所有目录和子目录下的txt 文件，并且是绝对路径
sub_full_txt = []
file_row_keyword = {}


def search_keyword(path, keyword):
    for folder, sub_folders, sub_files in os.walk(path):
        # 过滤出txt 文件
        sub_files_txt = list(filter(lambda x: os.path.splitext(x)[1] == '.txt', sub_files))
        # 转换成绝对路径的txt 文件
        sub_full_txt.extend(os.path.join(folder, each_file) for each_file in sub_files_txt)

    for file_name in sub_full_txt:
        f_open = open(file_name, 'r', encoding='utf-8')
        f_lines = f_open.readlines()
        f_open.close()

        # 预先定义一个子字典存储行数和关键字位置关系信息
        row_keyword = {}

        for row_number in range(len(f_lines)):
            f_keyword_pos_dic = []
            start_search_pointer = 0
            f_keyword_pos = f_lines[row_number].find(keyword, start_search_pointer)

            while f_keyword_pos >= 0:
                f_keyword_pos_dic.append(f_keyword_pos)
                start_search_pointer = f_keyword_pos + 1
                f_keyword_pos = f_lines[row_number].find(keyword, start_search_pointer)

                # 在一行中，关键字查找结束
                if f_keyword_pos == -1:
                    row_keyword.setdefault(row_number+1, f_keyword_pos_dic)
                    if file_name in file_row_keyword.keys():
                        file_row_keyword[file_name] = row_keyword
                    else:
                        file_row_keyword.setdefault(file_name, row_keyword)

    # 函数返回一个字典，key=文件路径，value=（以行数为key，以位置信息列表为value 的字典），如下
    # {
    #   'C:/Users/felix_yang/PycharmProjects/learningpython\\28\\record.txt': {5: [16], 6: [4]},
    #  'C:/Users/felix_yang/PycharmProjects/learningpython\\29\\boy_1.txt': {3: [0]},
    #  'C:/Users/felix_yang/PycharmProjects/learningpython\\29\\boy_2.txt': {3: [0]},
    #  'C:/Users/felix_yang/PycharmProjects/learningpython\\29\\girl_1.txt': {3: [12, 23], 7: [12, 23]}
    # }

    return file_row_keyword


if __name__ == '__main__':
    filename = input('请输入待查找的初始目录：')
    keyword = input('请输入需要查找的关键字：')
    search_keyword(filename, keyword)
    for file_key in file_row_keyword.keys():
        print('============================================')
        print('在文件【%s】中找到关键字【%s】' % (file_key, keyword))
        for rows in file_row_keyword[file_key].keys():
            # 将字典存储的位置信息转换成字符串打印
            key_str = [str(i) for i in file_row_keyword[file_key][rows]]
            print('关键字出现在第 %d 行，第 【 %s 】 位置' % (rows, ','.join(key_str)))
