# 编写一个函数，判断传入的字符串参数是否为“回文联”

# list的reverse()方法是返回None的，只会对列表内的元素逆序排序。而string的reserved()方法是会返回逆序后的字符串的

def check(var):
    list1 = list(var)
    list2 = list1[:]
    list2.reverse()

    if list1 == list2:
        print('传入的参数 %s 是：回文联' % var)
    else:
        print('传入的参数 %s 不是：回文联' % var)


check('1234321')

