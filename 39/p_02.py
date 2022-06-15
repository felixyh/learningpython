# 定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构
#
# 方法：
# - isEmpty():判断当前栈是否为空（返回True或Talse）
# - push():往栈的顶部压入一个数据项
# - pop():从栈顶弹出一个数据项（并在栈中删除）
# - top():显示当前栈顶的一个数据项
# - bottom():显示当前栈底的一个数据项

class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, x):
        self.data.append(x)

    def pop(self):
        self.data.pop()

    def top(self):
        try:
            print(self.data[-1])
        except IndexError:
            print('no data in stack')

    def bottom(self):
        try:
            print(self.data[0])
        except IndexError:
            print('no data in stack')
