# 定义一个单词（Word）类继承自字符串，重写比较操作符，当两个 Word 类对象进行比较时，根据单词的长度来进行比较大小。
# >>> help(str.__lt__)
#
# >>> help(str.__gt__)
#
# >>> help(str.__eq__)
#
# >>> help(str.__ne__)
#
# >>> help(str.__le__)
#
# >>> help(str.__ge__)

class Word(str):
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


w1 = Word('123')
w2 = Word('3456')
print(w1 > w2)
print(w1 < w2)
print(w1 != w2)
print(w1 == w2)
print(w1 >= w2)
print(w1 <= w2)



