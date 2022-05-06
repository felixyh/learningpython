def power(x, y):
    if y == 0:
        return 1
    elif y > 0:
        if y == 1:
            return x
        else:
            result = x
            for i in range(y-1):
                result *= x
            return result
    else:
        if y == -1:
            return 1/x
        else:
            result = x
            for i in range((-y-1)):
                result *= x
            return 1/result

print(power(2, -2))
