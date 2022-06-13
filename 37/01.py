# 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
#
# - 平日票价100元
# - 周末票价为平日的120%
# - 儿童半票


class Ticket:
    def __init__(self, day, adult_count, child_count):
        self.day = day
        self.adult_count = adult_count
        self.child_count = child_count

    def price(self):
        if self.day == "WD":
            print('总票价为：{:.2f}'.format(100 * self.adult_count + 50 * self.child_count))
        elif self.day == "WED":
            print('总票价为：{:.2f}'.format((100 * self.adult_count + 50 * self.child_count) * 1.2))


ticket1 = Ticket('WD', 2, 1)
ticket1.price()

