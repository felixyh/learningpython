# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。

# 设定初始值为7级台阶
stage = 7

# 算出的符合条件的结果，当为1 的时候，表示第一个算出的，也是至少有多少级台阶
result = 0

while stage > 0 and result != 1:
    if (stage % 7 == 0) and (stage % 2 == 1) and (stage % 5 == 4) and (stage % 6 == 5):
        print('至少有 %d 级台阶' % stage)
        result = 1
    stage += 7







