import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('我现在的位置是：', self.x, self.y)


class GoldFish(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        # 使用super函数
        super().__init__()
        self.hungary = True

    def eat(self):
        if self.hungary:
            print('我好饿，吃，吃，吃')
            self.hungary = False
        else:
            print('我已经吃饱啦！')







