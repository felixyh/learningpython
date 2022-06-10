# 按照以下提示尝试定义一个Person类并生成类实例对象。
# 属性：姓名（默认姓名为“小甲鱼”）
# 方法：打印姓名
# 提示：方法中对属性的引用形式需加上self，如self.name

class Person:
    name = '小甲鱼'

    def printname(self):
        print(self.name)


p1 = Person()
p1.name = 'FishC'
p1.printname()


