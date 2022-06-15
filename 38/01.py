# 定义一个点（Point）类和直线（Line）类，使用 getLen 方法可以获得直线的长度。
#
# 提示：
#
# - 设点 A(X1,Y1)、点 B(X2,Y2)，则两点构成的直线长度 |AB| = √((x1-x2)2+(y1-y2)2)
# - Python 中计算开根号可使用 math 模块中的 sqrt 函数
# - 直线需有两点构成，因此初始化时需有两个点（Point）对象作为参数


import math as m


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line(Point):
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def getLen(self):
        return m.sqrt((self.point_a.x-self.point_b.x)**2 + (self.point_a.y-self.point_b.y)**2)


point_a = Point(1, 3)
point_b = Point(1, 5)
line = Line(point_a, point_b)
print(line.getLen())
