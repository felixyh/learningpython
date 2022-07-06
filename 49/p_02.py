# 如果你的策略是将 2000000 以内的所有素数找到并存放到一个列表中，再依次进行求和计算，
# 那么这个列表极有可能会撑爆你的内存。所以这道题就必须用到生成器来实现啦。

import math as m


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            for current in range(3, int(m.sqrt(number)+1), 2):
                if number % current == 0:
                    return False
            return True
    else:
        return False


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == '__main__':
    solve()





