# 要求自己写一个 MyRev 类，功能与 reversed() 相同（内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）
# 例如：
# >>> myRev = MyRev("FishC")
# >>> for i in myRev:
#     print(i, end='')
#
# ChsiF

class MyRev:
    def __init__(self, item):
        self.item = item
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            temp = self.item[self.index]
            self.index -= 1
        except IndexError:
            raise StopIteration
        return temp




