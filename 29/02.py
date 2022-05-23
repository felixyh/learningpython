# 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置，程序实现如图：

name1 = input('请输入需要比较的头一个文件名：')
name2 = input('请输入需要比较的另一个文件名：')

name1_f = open(name1, 'rt')
name2_f = open(name2, 'rt')

name1_list = name1_f.readlines()
name2_list = name2_f.readlines()

name1_f.close()
name2_f.close()


diff_count = []
name1_len = len(name1_list)
name2_len = len(name2_list)


if name1_len >= name2_len:
    file_min_len = name2_len
else:
    file_min_len = name1_len


for i in range(file_min_len):
    if name1_list[i] != name2_list[i]:
        diff_count.append(i)


print('两个文件共有【 %d 】处不同：' % len(diff_count))

for each in diff_count:
    print('第 %d 行不一样' % each)

