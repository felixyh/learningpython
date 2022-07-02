#!/usr/bin/python
# -*- coding:utf-8 -*-
import time as t


class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.borrow = [1, 12, 31, 24, 60, 60]
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()结束计时！"
        print("计时开始……")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            temp = self.end[index] - self.begin[index]
            # 低位不够减，需要向高位借位
            if temp < 0:
                # 测试高位是否有得借，没得借的话再向高位借……
                i = 1
                while self.lasted[index-i] < 1:
                    self.lasted[index-i] += self.borrow[index-i] - 1
                    self.lasted[index-i-1] -= 1
                    i += 1
                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index-1] -= 1
            else:
                self.lasted.append(temp)

        # 由于高位随时会被借位，所以打印要放在最后
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]

        # 为下一轮计算初始化变量
        self.begin = 0
        self.end = 0
        print(self.prompt)

    # 调用实例直接显示结果
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    # 计算两次计时器对象之和
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt


t1 = MyTimer()
t2 = MyTimer()
t1.start()
t.sleep(65)
t1.stop()
t2.start()
t.sleep(15)
t2.stop()
print(t1 + t2)