# 编写一个程序，这次要求使用pickle将文件（ record.txt (1.1 KB, 下载次数: 3561) ）里的对话按照以下要求腌制成不同文件（没错，是第29讲的内容小改，考考你自己能写出来吗？）：
#             ※小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
#             ※小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
#             ※文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件
#             （提示：文件中不同的对话间已经使用“==========”分割）


import pickle


def extract(file_name):
    count = 0
    boy_list = []
    girl_list = []
    record_file = open(file_name, 'r')
    for each_line in record_file:
        # people, words = tuple(each_line.split(':'))
        # if people == '小甲鱼':
        #     boy_list.append(words)
        # elif people == '小客服':
        #     girl_list.append(words)
        temp_list = each_line.split(':')
        if temp_list[0] == '小甲鱼':
            boy_list.append(temp_list[1])
        elif temp_list[0] == '小客服':
            girl_list.append(temp_list[1])

        if '========' in each_line:
            count += 1
            pickle_file_boy = open('boy_%d.txt' % count, 'wb')
            pickle_file_girl = open('girl_%d.txt' % count, 'wb')
            pickle.dump(boy_list, pickle_file_boy)
            pickle.dump(girl_list, pickle_file_girl)
            pickle_file_boy.close()
            pickle_file_girl.close()
            boy_list = []
            girl_list = []
    count += 1
    pickle_file_boy = open('boy_%d.txt' % count, 'wb')
    pickle_file_girl = open('girl_%d.txt' % count, 'wb')
    pickle.dump(boy_list, pickle_file_boy)
    pickle.dump(girl_list, pickle_file_girl)
    pickle_file_boy.close()
    pickle_file_girl.close()

    record_file.close()


extract('record.txt')