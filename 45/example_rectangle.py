# 课堂练习
#
# - 写一个矩形类，默认有宽和高两个属性
# - 如果为一个叫square的属性赋值，那么说明是一个正方形，值就是正方形的边长，此时宽和高都应该等于边长

class Rectangle:
    def __init__(self):
        self.width = 5
        self.height = 8

    def __setattr__(self, name, value):
        if name == 'square':
            print('it is a square!!')
            self.width = value
            self.height = value
        # 继承默认基类的方法，给属性赋值；如果不写，会出现死循环
        super().__setattr__(name, value)

        # 还可以通过默认属性字典的方式，直接给属性赋值
        # self.__dict__[name] = value



rec = Rectangle()
print(rec.width, rec.height)

rec.square = 10
print(rec.square, rec.width, rec.height)
