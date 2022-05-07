def discounts(price, rate):
    final_price = price * rate
    # old_price = 88  # 这里试图修改全局变量
    # print('修改后的old_price的值是：', old_price)
    # 试图打印全局变量: old_price 不会报错
    print('试图打印全局变量old_price', old_price)
    return final_price


old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)
#print('修改后的old_price的值是：', old_price)
print('打折扣价格是：', new_price)

