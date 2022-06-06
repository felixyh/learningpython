# 写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？
# 要求一：递归搜索各个文件夹 要求二：显示各个类型的源文件和源代码数量 要求三：显示总行数与百分比

import easygui as g
import sys
import os
import os.path


def code_cal(dir_path):
    format_list = ['.py', '.tf', '.sh']
    code_lines = 0
    ext_dic = {'.py': [0, 0], '.tf': [0, 0], '.sh':[0, 0]}

    # os.walk() 返回的是一个三元组迭代器，有三元组参数，通过for 循环使用
    for folder, sub_folders, sub_files in os.walk(dir_path):
        for each_file in sub_files:
            ext_temp = os.path.splitext(each_file)[1]

            if ext_temp in format_list:

                ext_dic[ext_temp][0] += 1

                with open(os.path.join(folder, each_file), 'r') as f_py:
                    len_temp = len(f_py.readlines())
                    ext_dic[ext_temp][1] += len_temp
                    code_lines += len_temp

    return code_lines, ext_dic


f_path = g.diropenbox(msg=None, title=None, default=None)

if f_path:
    total_lines, ext_row_line = code_cal(f_path)
    message = '您目前共累计编写了 {0} 行代码，完成进度 {1:.2%} \n 离 {2} 行代码还差 {3} 行，请继续努力'.format(
        total_lines,
        total_lines/100000,
        100000,
        100000-total_lines
    )
    text_title = '统计结果'
    text_content = ''
    for each in ext_row_line.keys():
        text_content += '[{0}]源文件 {1} 个，源代码 {2} 行 \n'.format(
            each,
            ext_row_line[each][0],
            ext_row_line[each][1]
        )
    g.textbox(msg=message, title=text_title, text=text_content)
else:
    sys.exit()


