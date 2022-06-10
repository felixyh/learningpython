try:
    sum_umber = 1 + '1'
    f = open('我为什么是个文件.txt')
    print(f.read())
    f.close()
except (OSError, TypeError):
    print('文件出错啦@')
