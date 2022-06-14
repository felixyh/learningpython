# 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。（初学者不一定可以完整实现，但请务必先自己动手，你会从中学习到很多知识的^_^）
#
# - 假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
# - 游戏生成1只乌龟和10条鱼
# - 它们的移动方向均随机
# - 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# - 当移动到场景边缘，自动向反方向移动
# - 乌龟初始化体力为100（上限）
# - 乌龟每移动一次，体力消耗1
# - 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# - 鱼暂不计算体力
# - 当乌龟体力值为0（挂掉）或者鱼儿的数量为0, 游戏结束

import random as r


class Turtle:
    def __init__(self, energy, position):
        self.XY_list = ['X', 'Y']
        self.direction_list = ['forward', 'backward']
        self.move_param = None
        self.move_points = None
        self.energy = 100
        self.position = {self.XY_list[0]: r.randint(0, 10), self.XY_list[1]: r.randint(0, 10)}
        print('Turtle initial position is [{:d}, {:d}]'.format(self.position['X'], self.position['Y']))

    def move(self):
        self.move_points = r.randint(1, 2)
        self.move_param = (r.choice(self.XY_list), r.choice(self.direction_list))
        if self.move_param[1] == 'forward':
            self.position[self.move_param[0]] += self.move_points
            if self.position[self.move_param[0]] > 10:
                self.position[self.move_param[0]] = 20 - self.position[self.move_param[0]]
        else:
            self.position[self.move_param[0]] -= self.move_points
            if self.position[self.move_param[0]] < 0:
                self.position[self.move_param[0]] = 0 - self.position[self.move_param[0]]
        return self.position
        print('Turtle moved once, now new position is [{:d}, {:d}]'.format(self.position['X'], self.position['Y']))


class Fish:
    def __init__(self):
        self.XY_list = ['X', 'Y']
        self.direction_list = ['forward', 'backward']
        self.position = {self.XY_list[0]: r.randint(0, 10), self.XY_list[1]: r.randint(0, 10)}
        self.move_param = None
        self.move_points = 1

    def move(self):
        self.move_param = (r.choice(self.XY_list), r.choice(self.direction_list))
        if self.move_param[1] == 'forward':
            self.position[self.move_param[0]] += self.move_points
            if self.position[self.move_param[0]] > 10:
                self.position[self.move_param[0]] = 20 - self.position[self.move_param[0]]
        else:
            self.position[self.move_param[0]] -= self.move_points
            if self.position[self.move_param[0]] < 0:
                self.position[self.move_param[0]] = 0 - self.position[self.move_param[0]]
        return self.position
        print('Fish moved once, now new position is [{:d}, {:d}]'.format(self.position['X'], self.position['Y']))


# 生成10条小鱼和1只乌龟
turtle = Turtle()
fish = []
for i in range(0, 10):
    fish[i] = Fish()





