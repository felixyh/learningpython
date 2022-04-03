# 判断闰年
# 能被4整除但不能被100整除,或者能被400整除都是闰年。

temp = input('清输入一个年份：')
while not temp.isdigit():
    temp = input('输入的不是年份，清重新输入：')

year = int(temp)

# 采用取余数的方法
if (year % 4 == 0) and (year % 100 != 0):
    print('%d 是闰年' % year)
else:
    if year % 400 == 0:
        print('%d 是闰年' % year)
    else:
        print('%d 不是闰年' % year)
