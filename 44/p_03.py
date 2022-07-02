# 既然咱都做到这一步，那不如深入一下，再次改进我们的代码，让它能够统计一个函数运行若干次的时间
#
# 要求一：函数调用的次数可以设置（默认是1000000次）
#
# 要求二：新增一个 timeing()方法，用于启动计时器

# !/usr/bin/python
# -*- coding:utf-8 -*-

import time as t


class MyTimer:
    def __init__(self, func, number=1000000):
        self.prompt = "未开始计时"
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter
        self.number = number
        self.func = func

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了%0.2f秒" % result
        return prompt

    # 内置方法，计算运行时间
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.number):
            self.func()
        self.end = self.default_timer()
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了 %0.2f 秒" % self.lasted

    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效")


def test():
    text = "I love FishC.com!"
    char = 'o'
    if char in text:
        pass


t1 = MyTimer(test)
t1.timing()
print(t1)
t2 = MyTimer(test, 10000000)
t2.timing()
print(t2)
t3 = MyTimer(test, 100000000)
t3.timing()
print(t3)
