# 按照以下要求，定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度 = 摄氏度*1.8+32）
#
# 要求：我们希望这个类尽量简练地实现功能，如下
#
# >>> print(C2F(32))
# 89.6

class C2F(float):
    def __new__(cls, c_number):
        c_number = c_number * 1.8 + 32
        return float.__new__(cls, c_number)


print(C2F(32))
