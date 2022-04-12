# 3. 三色球问题
#
# > 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，蓝球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。


# x + y + z = 8
# x is red, y is yellow, z is blue

for x in range(0, 4):
    for y in range(0, 4):
        for z in range(2, 7):
            if x + y + z == 8:
                print('totally we can have %d red, %d yellow, %d blue' % (x, y, z))

