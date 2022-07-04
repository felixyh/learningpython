# 定义一个不可改变的列表，且可以记录每个元素的访问次数。

class MyList:
    # python中很有趣的两个小东西，先介绍：
    # 1、*args保存多余变量，保存方式为元组。
    # 2、**args保存带有变量名的多余变量，保存方式为字典。
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
        # 这里使用列表的下标作为字典的键，注意不能用元素作为字典的键
        # 因为列表的不同下标可能有值一样的元素，但字典不能有两个相同的键

    def __len__(self):
        return len(self.count)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]


list1 = MyList(1, 3, 4)
list1[0]
list1[1]
list1.count



