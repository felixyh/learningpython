# 写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？
# 要求一：递归搜索各个文件夹 要求二：显示各个类型的源文件和源代码数量 要求三：显示总行数与百分比

import easygui as g
import sys
import os
import os.path


def code_cal(dir_path):
    format_list = ['.py', '.tf', '.sh']
    code_lines = 0
    ext_dic = dict.fromkeys(format_list, [0, 0])
    print(ext_dic)
    # os.walk() 返回的是一个三元组迭代器，有三元组参数，通过for 循环使用
    for folder, sub_folders, sub_files in os.walk(dir_path):
        for each_file in sub_files:
            ext_temp = os.path.splitext(each_file)[1]
            print(os.path.join(folder, each_file))
            print(ext_temp)
            # if ext_temp in format_list:
            #     print(os.path.join(folder, each_file))
            #     print(ext_dic['.py'], ext_dic['.sh'], ext_dic['.tf'])
            #     print(ext_temp)
            #     print(ext_dic[ext_temp])
            #     ext_dic[ext_temp][0] += 1
            #     print(ext_dic['.py'], ext_dic['.sh'], ext_dic['.tf'])
            #     with open(os.path.join(folder, each_file), 'r') as f_py:
            #         len_temp = len(f_py.readlines())
            #         ext_dic[ext_temp][1] += len_temp
            #         code_lines += len_temp
            #         print(ext_dic['.py'], ext_dic['.sh'], ext_dic['.tf'])
            # print(ext_dic['.py'], ext_dic['.sh'], ext_dic['.tf'])
            if ext_temp == '.py':
                ext_dic['.py'][0] += 1
                with open(os.path.join(folder, each_file), 'r') as f_tmp:
                    len_temp = len(f_tmp.readlines())
                    ext_dic['.py'][1] += len_temp
                    code_lines += len_temp

            elif ext_temp == '.tf':
                ext_dic['.tf'][0] += 1
                with open(os.path.join(folder, each_file), 'r') as f_tmp:
                    len_temp = len(f_tmp.readlines())
                    ext_dic['.tf'][1] += len_temp
                    code_lines += len_temp
            elif ext_temp == '.sh':
                ext_dic['.sh'][0] += 1
                with open(os.path.join(folder, each_file), 'r') as f_tmp:
                    len_temp = len(f_tmp.readlines())
                    ext_dic['.sh'][1] += len_temp
                    code_lines += len_temp

    return code_lines, ext_dic


f_path = g.diropenbox(msg=None, title=None, default=None)

if f_path:
    total_lines, ext_row_line = code_cal(f_path)
    print(ext_row_line)
    message = '您目前共累计编写了 %d 行代码，完成进度 %d \n 离 %d 行代码还差 %d 行，请继续努力' % (total_lines, total_lines/100000, 100000, 100000-total_lines)
    text_title = '统计结果'
    text_content = ''
    for each in ext_row_line.keys():
        text_content += '[%s]源文件 %d 个，源代码 %d 行 \n' % (each, ext_row_line[each][0], ext_row_line[each][1])
    g.textbox(msg=message, title=text_title, text=text_content, codebox='', callback=None, run=True)
else:
    sys.exit()


