# 例子：现在要定一个类，叫水池，水池里要有乌龟和鱼

class Turtle:
    def __init__(self, x):
        self.number = x


class Fish:
    def __init__(self, x):
        self.number = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池里总共由%d只乌龟，%d只鱼' %(self.turtle.number, self.fish.number))


p1 = Pool(1, 2)
p1.print_num()

