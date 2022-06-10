try:
    f = open('我为什么是个文件.txt', 'w')
    f.write('我存在了！')
    sum_umber = 1 + '1'

except (OSError, TypeError):
    print('文件出错啦@')
finally:
    f.close()
