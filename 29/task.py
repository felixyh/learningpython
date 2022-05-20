# 任务：将文件(record.txt)中的数据进行分割，并按照以下规则保存起来。
#  1.小甲鱼的对话单独保存为boy_*.txt的文件(去掉"小甲鱼:")
#  2.小客服的对话单独保存为girl_*.txt的文件(去掉"小客服:")
#  3.文件中总共有三段对话，分别保存为boy_1.txt、boy_2.txt、boy_3.txt、gilr_1.txt、gilr_2.txt、gilr_3.txt
#    共6个文件。(提示：不同的对话已经使用"===="进行分割)


f1 = open('../28/record.txt', 'rt')
count = 1

boy_list = []
girl_list = []


def generate_file(file_name, file_list):
    f_file_name = open(file_name, 'x')
    f_file_name.writelines(file_list)
    f_file_name.close()


for each_line in f1:
    temp_list = each_line.split(':')
    if temp_list[0] == '小甲鱼':
        boy_list.append(temp_list[1])
    elif temp_list[0] == '小客服':
        girl_list.append(temp_list[1])

    if "====" in each_line:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        generate_file(file_name_boy, boy_list)
        generate_file(file_name_girl, girl_list)

        boy_list = []
        girl_list = []
        count += 1


# 循环结束，写入最后一段内容
file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'

generate_file(file_name_boy, boy_list)
generate_file(file_name_girl, girl_list)


# 关闭原始文件
f1.close()







