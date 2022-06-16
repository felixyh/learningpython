# class C:
#     def __init__(self, size=10):
#         self.size = size
#
#     def getSize(self):
#         return self.size
#
#     def setSize(self, value):
#         self.size = value
#
#     def delSize(self):
#         del self.size
#
#     x = property(getSize, setSize, delSize)

# 通过自学【扩展阅读】property 的详细使用方法，将上面的代码修改为“使用属性修饰符创建描述符”的方式实现

class C:
    def __init__(self, size=10):
        self.size = size

    @property
    def size(self):
        """I'm the 'x' property."""
        return self.size

    @size.setter
    def size(self, value):
        self.size = value

    @size.deleter
    def size(self):
        del self.size
