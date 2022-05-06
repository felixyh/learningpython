# 编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
# 例如：假定输入的字符串为
# “You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”，
# 子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。

def findstr(x, y):
    a = y[0]
    b = y[1]
    count = 0
    xlen = len(x)
    for i in range(xlen):
        if x[i] == a and x[i+1] == b:
            count += 1
    print(count)


findstr('You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.', 'im')

