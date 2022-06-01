try:
    f = open('我为什么是个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦@ \n错误的原因是：' + str(reason))