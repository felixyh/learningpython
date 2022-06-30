# 案例
#
# - 定制一个计时器的类
# - start和stop 方法代表启动计时器和停止计时器
# - 假设计时器对象t1，print(t1) 和直接调用t1均显示结果
# - 当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
# - 两个计时器对象可以进行相加：t1+t2
# - 只能使用提供的有限资源完成

class MyTimer:
    def __add__(self, other):
        return float(self) + float(other)

    def start(self):
        pass

    def stop(self):
        pass



