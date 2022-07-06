# 如果你的策略是将 2000000 以内的所有素数找到并存放到一个列表中，再依次进行求和计算，
# 那么这个列表极有可能会撑爆你的内存。所以这道题就必须用到生成器来实现啦。


def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            break
        else:
            return True


def get_prime():
    number = 2
    while number < 2000000:
        if is_prime(number):
            yield number
        number += 1


prime = get_prime()
total = 0
for x in prime:
    total += x
print(total)

