# 按照以下提示尝试定义一个矩阵类并生成类实例对象。
#
# 属性：长和宽
#
# 方法：设置长和宽->setRect(self)，获得长和宽->getRect(self)，获得面积->getArea(self)
#
# 提示：方法中对属性的引用形式需加上self，如self.width

class Rectangle:

    def __init__(self):
        self.width = None
        self.length = None

    def set_rect(self):
        print('请输入矩形的长和宽...')
        self.length = float(input('长：'))
        self.width = float(input('宽：'))

    def get_rect(self):
        print('这个矩形的长是：{0:.2f} 宽是：{1:.2f}'.format(self.length, self.width))

    def get_area(self):
        return self.length * self.width


rect = Rectangle()
rect.set_rect()
rect.get_rect()
rect.get_area()

