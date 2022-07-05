# fibonacci 数列的迭代器魔法方法实现

class fibonacci:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.b < self.n:
            self.a, self.b = self.b, self.a + self.b
        else:
            raise StopIteration
        return self.a

