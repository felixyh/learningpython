# 修改上边【测试题】第 4 题，使之可以正常运行：编写一个 Counter 类，用于实时检测对象有多少个属性。、
#
# 程序实现如下：

# >>> c = Counter()
# >>> c.x = 1
# >>> c.counter
# 1
# >>> c.y = 1
# >>> c.z = 1
# >>> c.counter
# 3
# >>> del c.x
# >>> c.counter
# 2


# 此方法有一个bug，其实不是检测的某个对象的属性数量，而是检测整个类的所有对象的属性数量。。。

class Counter:
    counter = 0

    def __setattr__(self, name, value):
        Counter.counter += 1
        super().__setattr__(name, value)

    def __delattr__(self, name):
        Counter.counter -= 1
        super().__delattr__(name)

c = Counter()
c.x = 1
print(c.counter)
c.y = 1
c.z = 1
print(c.counter)
del c.x
print(c.counter)

