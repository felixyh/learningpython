# 案例
#
# - 定制一个计时器的类
# - start和stop 方法代表启动计时器和停止计时器
# - 假设计时器对象t1，print(t1) 和直接调用t1均显示结果
# - 当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
# - 两个计时器对象可以进行相加：t1+t2
# - 只能使用提供的有限资源完成
import time
import time as t


class MyTimer:
    def __init__(self, status=0):
        self.start_time = None
        self.stop_time = None
        self.status = status

    def start(self):
        self.start_time = t.localtime()
        self.status = 1

    def stop(self):
        if self.status == 0:
            print('计时器未启动')
        else:
            self.stop_time = t.localtime()
            self.status = 0

    def __repr__(self):
        self.interval_sec = self.stop_time.tm_sec - self.start_time.tm_sec
        self.interval_min = self.stop_time.tm_min - self.start_time.tm_min
        self.interval_hour = self.stop_time.tm_hour - self.start_time.tm_hour
        self.interval = (self.interval_hour * 60 + self.interval_min) * 60 + self.interval_sec
        return str(self.interval)

    def __str__(self):
        self.interval_sec = self.stop_time.tm_sec - self.start_time.tm_sec
        self.interval_min = self.stop_time.tm_min - self.start_time.tm_min
        self.interval_hour = self.stop_time.tm_hour - self.start_time.tm_hour
        self.interval = (self.interval_hour * 60 + self.interval_min) * 60 + self.interval_sec
        return str(self.interval)

    def __add__(self, other):
        return float(self.__repr__()) + float(other.__repr__())





