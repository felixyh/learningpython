# 按要求重写魔法方法：当访问一个不存在的属性时，不报错且提示“该属性不存在！”

class C:
    def __getattr__(self, item):
        print('该属性不存在！')

