# 要求实现一个功能与 reversed() 相同（内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）的生成器
#
# >>> for i in myRev("FishC"):
#     print(i, end='')
#
# ChsiF

def myRev(seq):
    seq_len = len(seq)
    index = -1
    while index >= -seq_len:
        temp = seq[index]
        yield temp
        index -= 1


for i in myRev("FishC"):
    print(i, end='')

