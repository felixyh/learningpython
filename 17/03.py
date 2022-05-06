def biner(x):
    binarylist = []
    while x != 0:
        flag = str(x % 2)
        binarylist.insert(0, flag)
        x = x // 2
    # 将列表或元组转换成字符串的方法：''.join(object)
    return ''.join(binarylist)

print(biner(4))