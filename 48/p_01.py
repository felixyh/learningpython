# 用 while 语句实现与以下 for 语句相同的功能：
#
# for each in range(5):
#     print(each)

it = iter(range(5))
while True:
    try:
        each = next(it)

    except StopIteration:
        break

    print(each)





