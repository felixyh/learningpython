# 第二个例子：课堂练习
#
# - 先定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性。
# - 要求两个属性会自动进行转换，也就是说你可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果。
#   公式：摄氏度 * 1.8 + 32 = 华氏度

class Cproperty:
    def __init__(self, c_convert, c_set, c_del):
        self.c_convert = c_convert
        self.c_set = c_set
        self.c_del = c_del

    def __get__(self, instance, owner):
        self.c_convert(instance)

    def __set__(self, instance, value):
        self.c_convert(instance, value)

    def __delete__(self, instance):
        pass


class Fproperty:
    def __init__(self, f_convert, f_set, f_del):
        self.f_convert = f_convert
        self.f_set = f_set
        self.f_del = f_del

    def __get__(self, instance, owner):
        return self.f_convert(instance)

    def __set__(self, instance, value):
        self.f_convert(instance, value)

    def __delete__(self, instance):
        pass


class Temperature:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def celsius_get(self):
        return self.temperature

    def celsius_set(self, value):
        self.temperature = value

    def celsius_del(self):
        del self.temperature

    def fahrenheit_get(self):
        return self.temperature

    def fahrenheit_set(self, value):
        self.temperature = value

    def fahrenheit_del(self):
        del self.temperature

    c = Cproperty(celsius_get, celsius_set, celsius_del)
    f = Fproperty(fahrenheit_get, fahrenheit_set, fahrenheit_del)