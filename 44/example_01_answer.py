import time
import time as t


class MyTimer:
    def __init__(self):
        # 定义一个列表存放时间的单位，以便程序运行后输出的结果直接是带单位的结果：如：总共运行了：3秒
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = '未开始计时！'
        self.lasted = []
        # self.start = 0
        self.begin = 0
        # self.stop = 0
        self.end = 0
        # 这里特别需要注意，方法名和属性名不能定义成同一个名字，否则属性会覆盖方法

    # 实现直接调用对象来输出内容
    def __str__(self):
        return self.prompt

    # __str__ 赋值给 __repr__
    __repr__ = __str__

    # 两个对象相加
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:  # 如果result是空的话执行
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    # 开始计时
    def start(self):  # self表示对象的引用
        self.begin = t.localtime()
        self.prompt = '提示：请先调用stop()停止计时'
        print('计时开始...')

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()进行计时！")
        else:
            self.end = t.localtime()
            # 结束计时时并进行计算，即对象.内部方法
            self._clac()
            print('计时结束！')

    # 内部方法(_方法名)，计算运行时间
    def _clac(self):
        # 计算的结果放在一个列表里面
        self.lasted = []
        # 定义一个提示的变量
        self.prompt = '总共运行了'
        # 依次遍历localtime的索引
        for index in range(6):
            # 用结束时间减去开始时间得到运行的时间，并把结果放到lasted[]列表内
            self.lasted.append(self.end[index] - self.begin[index])
            # 把每一次计算的结果进行一次追加
            if self.lasted[index]:  # 当lasted为0时就不会执行if内的语句，而是执行下一轮的循环
                self.prompt += str(self.lasted[index]) + self.unit[index]  # 运行时间+单位

                # 为下一轮计时初始化变量
                self.begin = 0
                self.end = 0
