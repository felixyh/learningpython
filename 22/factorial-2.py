def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


number = int(input('please input a number:'))
final_result = factorial(number)
print(final_result)

