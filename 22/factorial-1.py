def factorial(x):
    result = x
    for n in range(1, x):
        result *= n
    return result


number = int(input('please input a number:'))
final_result = factorial(number)
print(final_result)

