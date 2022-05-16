# 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5]


def get_digits(n):
    result = []
    if n == 0:
        return []
    else:
        result.extend(get_digits(n // 10))
        result.append(n % 10)
        return result


print(get_digits(12342321421321))

