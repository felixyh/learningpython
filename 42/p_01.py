# 我们都知道在 Python 中，两个字符串相加会自动拼接字符串，
# 但遗憾的是两个字符串相减却抛出异常。
# 因此，现在我们要求定义一个 Nstr 类，支持字符串的相减操作：A – B，从 A 中去除所有 B 的子字符串。

class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')


s1 = Nstr('felixyangfelixyang')
s2 = Nstr('felix')
print(s1 - s2)


