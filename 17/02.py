def gcder(a, b):
    flag = a % b
    result = b
    while flag != 0:
        flag = a % b
        result = b
        a = b
        b = flag
    return result

print(gcder(121, 11))

