try:
    f = open('test.txt', 'w')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('出错啦！' + str(reason))
finally:
    f.close()