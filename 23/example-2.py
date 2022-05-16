def fibonacci(n):
    n1 = 1
    n2 = 1

    if n < 1:
        print('The number is incorrect')

    elif n == 1 or n == 2:
        return 1
    else:
        while (n-2) > 0:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            n -= 1
        return n3


n = int(input('please input a number:'))
result = fibonacci(n)
print(result)


