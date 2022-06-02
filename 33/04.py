try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    try:
        f.close()
    except NameError as reason:
        print('出错啦：' + str(reason))

