temp = input('请输入一个整数：')
number = int(temp)

# StarNumber = number
# SpaceNumber = number - 1

while number > 0:
    StarNumber = number
    SpaceNumber = number - 1
    print(' '*SpaceNumber + '*'*StarNumber)

    number = number - 1

