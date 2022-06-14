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
    def __init__(self, energy):
        self.init_position = None
        self.XY_list = ['X', 'Y']
        self.direction_list = ['forward', 'backward']
        self.message = ''
        self.move_param = None
        self.move_points = None
        self.energy = energy
        self.max_energy = 100
        self.position = {self.XY_list[0]: r.randint(0, 10), self.XY_list[1]: r.randint(0, 10)}
        print('Turtle initial position is [{:d}, {:d}], energy: {:d}'.
              format(self.position['X'], self.position['Y'], self.energy))

    def move(self, init_position):
        self.init_position = init_position
        self.move_param = (r.choice(self.XY_list), r.choice(self.direction_list))
        self.move_points = r.randint(1, 2)
        if self.move_param[1] == 'forward':
            self.position[self.move_param[0]] = self.init_position[self.move_param[0]] + self.move_points
            if self.position[self.move_param[0]] > 10:
                self.position[self.move_param[0]] = 20 - self.position[self.move_param[0]]
                self.message = '触顶反弹'
            print('乌龟沿着{:s}轴 前进了{:d}步，{:s}！！！！！！now new position is [{:d}, {:d}], energy: {:d}'
                  .format(self.move_param[0], self.move_points, self.message, self.position['X'], self.position['Y'], self.energy-1))
        else:
            self.position[self.move_param[0]] = self.init_position[self.move_param[0]] - self.move_points
            if self.position[self.move_param[0]] < 0:
                self.position[self.move_param[0]] = 0 - self.position[self.move_param[0]]
                self.message = '触底反弹'
            print('乌龟沿着{:s}轴 后退了{:d}步，{:s}！！！！！！now new position is [{:d}, {:d}], energy: {:d}'
                  .format(self.move_param[0], self.move_points, self.message, self.position['X'], self.position['Y'], self.energy-1))

        # 乌龟每移动一步，能量减少1
        self.energy -= 1

        # print('Turtle moved once, now new position is [{:d}, {:d}, energy: {:d}]'
        # .format(self.position['X'], self.position['Y'], self.energy))

        return self.position


class Fish:
    def __init__(self):
        self.init_position = None
        self.XY_list = ['X', 'Y']
        self.direction_list = ['forward', 'backward']
        self.message = ''
        self.position = {self.XY_list[0]: r.randint(0, 10), self.XY_list[1]: r.randint(0, 10)}
        self.move_param = None
        self.move_points = 1

        print('Fish initial position is [{:d}, {:d}]'.format(self.position['X'], self.position['Y']))

    def move(self, init_position):
        self.init_position = init_position
        self.move_param = (r.choice(self.XY_list), r.choice(self.direction_list))
        if self.move_param[1] == 'forward':
            self.position[self.move_param[0]] = self.init_position[self.move_param[0]] + self.move_points
            if self.position[self.move_param[0]] > 10:
                self.position[self.move_param[0]] = 20 - self.position[self.move_param[0]]
                self.message = '触顶反弹'
            print('小鱼沿着{:s}轴 前进了 {:d}步，{:s}！！！！！！now new position is [{:d}, {:d}]'
                  .format(self.move_param[0], self.move_points, self.message, self.position['X'], self.position['Y']))
        else:
            self.position[self.move_param[0]] = self.init_position[self.move_param[0]] - self.move_points
            if self.position[self.move_param[0]] < 0:
                self.position[self.move_param[0]] = 0 - self.position[self.move_param[0]]
                self.message = '触底反弹'
            print('小鱼沿着{:s}轴 后退了 {:d}步，{:s}！！！！！！now new position is [{:d}, {:d}]'
                  .format(self.move_param[0], self.move_points, self.message, self.position['X'], self.position['Y']))

        # print('Fish moved once, now new position is [{:d}, {:d}]'.format(self.position['X'], self.position['Y']))

        return self.position


print('------------------------------')
print('初始化游戏！！！')
print('生成1只乌龟和10条小鱼')
print('------------------------------')
# 生成1只乌龟和位置
turtle = Turtle(100)
turtle_position = turtle.position

# 鱼对象列表
fish = []

# key=鱼对象，value=鱼位置
fish_position = {}

# 生成10条小鱼和位置，分别放在列表和字典中
createVar = locals()
for i in range(10):
    createVar['fish'+str(i)] = Fish()
    fish.append(createVar['fish' + str(i)])
    fish_position.setdefault(fish[i], fish[i].position)


print(3 * '\n')
print('------------------------------')
print('游戏开始！！！')
print('------------------------------')
# 初始化鱼的数量
fish_count = len(fish_position)

init_round = 1

while fish_count > 0 and turtle.energy > 0:
    print('Game on-going, Round: [{:}]'.format(init_round))
    turtle_position = turtle.move(turtle_position)
    for each_fish in list(fish_position.keys()):
        fish_position[each_fish] = each_fish.move(fish_position[each_fish])
        # 当乌龟和鱼坐标重叠, 乌龟吃掉鱼,乌龟体力增加20
        if fish_position[each_fish] == turtle_position:
            fish_position.pop(each_fish)
            fish_count = len(fish_position)
            print('------------------------------')
            print('一条鱼在位置 [{:d}, {:d}] 被吃掉！还剩{:}'.format(turtle_position['X'], turtle_position['Y'], fish_count))
            print('------------------------------')

            turtle.energy += 20
            if turtle.energy >= turtle.max_energy:
                turtle.energy = turtle.max_energy
    init_round += 1
    print('\n')

if fish_count == 0:
    print('Game Over, Turtle win!!')
elif turtle.energy == 0:
    print('Game Over, Fish win!!')




