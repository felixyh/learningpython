def cp_file(fname1, fname2):
    name1_f = open(fname1, 'rt')
    name2_f = open(fname2, 'rt')

    diff_row = []
    count = 0
    row_number = 1
    for each_line in name1_f:
        if each_line != name2_f.readline():
            count += 1
            diff_row.append(row_number)
        row_number += 1
    name2_f.close()
    name2_f.close()
    if count == 0:
        print('两个文件相同')
    else:
        print('两个文件共有【 %d 】处不同：' % count)
        for each in diff_row:
            print('第 %d 行不一样' % each)


def cp_main():
    name1 = input('请输入需要比较的头一个文件名：')
    name2 = input('请输入需要比较的另一个文件名：')

    cp_file(name1, name2)


if __name__ == '__main__':
    cp_main()

