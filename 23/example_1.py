def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n < 1:
        return -1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = input('please input a number:')
result = fibonacci(int(n))
if result != -1:
    print(result)

