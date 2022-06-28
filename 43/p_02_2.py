# 加分项：实例化时如果传入的是带空格的字符串，则去第一个空格前的单词作为参数

class Word(str):
    def __new__(cls, word):
        # 注意必须要使用__new__方法，因为str 是不可变类型
        # 必须在创建的时候将他初始化
        if ' ' in word:
            print('Value contains the spaces, truncating to first space.')
            word = word[: word.index(' ')]
        return str.__new__(cls, word)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __ge__(self, other):
        return len(self) >= len(other)


w1 = Word('I love you')
w2 = Word('felix')
print(w1 > w2)
print(w1 < w2)
print(w1 != w2)
print(w1 == w2)
print(w1 >= w2)
print(w1 <= w2)