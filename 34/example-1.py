def showMaxFactor(number):
    count = number // 2
    while count > 1:
        if number % count == 0:
            print('%d 的最大约数是 %d' %(number, count))
            break
        count -= 1
    else:
        print('%d 是一个素数' % number)


num = int(input('please input a number:'))
showMaxFactor(num)

