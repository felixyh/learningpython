# 根据上面的例子，定制一个列表，同样要求记录列表中每个元素被访问的次数。并且支持append()、pop()、extand()原生列表所拥有的方法。
#
# 要求：
# 1. 实现获取、设置和删除一个元素的行为(删除一个元素的时候对应的计数器也会被删除)
# 2. 增加counter(index)方法，返回index参数所指定的元素记录的访问次数
# 3. 实现append()、pop()、remove()、insert()、clear()和reverse()方法(重写这些方法时要注意考虑计数器的对应改变)


class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()





