# 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含**"\*"**则不计算在内。

# password = "novirus"
# count = 0
# while True:
#     if count <= 2:
#         userInputPass = input('please input the password:')
#         if userInputPass == password:
#             print('your password input is correct! Congrats!')
#             break
#         else:
#             if '*' not in userInputPass:
#                 count += 1
#             print('your password input is incorrect, please input again!')
#
#     else:
#         print('you already input 3 times, the password input is frozen!')
#         break


# 优化一下上述程序

# password = "novirus"
# count = 3
# while True:
#     if count > 0:
#         userInputPass = input('please input the password:')
#         if userInputPass == password:
#             print('your password input is correct! Congrats!')
#             break
#         elif '*' not in userInputPass:
#             count -= 1
#             print('your password input is incorrect, you have %d tries left' % count)
#         else:
#             print('your password input is incorrect, you have %d tries left' % count)
#             continue
#     else:
#         print('you already input 3 times, the password input is frozen!')
#         break


## 进一步优化

password = "novirus"
count = 3
while count:
    userInputPass = input('please input the password:')
    if userInputPass == password:
        print('your password input is correct! Congrats!')
        break
    elif '*' in userInputPass:
        print('your password input is incorrect, you have %d tries left' % count )
        continue
    else:
        print('your password input is incorrect, you have %d tries left' % (count-1))
    count -= 1

