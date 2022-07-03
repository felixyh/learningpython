# 第二个例子：课堂练习
#
# - 先定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性。
# - 要求两个属性会自动进行转换，也就是说你可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果。
#   公式：摄氏度 * 1.8 + 32 = 华氏度

class Cproperty:
    def __init__(self, c_get, c_set, c_del):
        self.c_get = c_get
        self.c_set = c_set
        self.c_del = c_del

    def __get__(self, instance, owner):
        return self.c_get(instance)

    def __set__(self, instance, value):
        self.c_set(instance, value * 1.8 + 32)


class Fproperty:
    def __init__(self, f_get, f_set, f_del):
        self.f_get = f_get
        self.f_set = f_set
        self.f_del = f_del

    def __get__(self, instance, owner):
        return self.f_get(instance)

    def __set__(self, instance, value):
        self.f_set(instance, (value - 32)//1.8)



class Temperature:
    def __init__(self, temperature=0):
        self.temperature = float(temperature)

    def gettemperature(self):
        return self.temperature

    def settemperature(self, value):
        self.temperature = float(value)

    c = Cproperty(gettemperature, settemperature, deltemperature)
    f = Fproperty(gettemperature, settemperature, deltemperature)