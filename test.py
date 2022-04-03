# class Turtle:
#
#     color = "green"
#     legs = 4
#
#     def climb(self):
#         print("I am climbing")
#
#     def run(self):
#         print("I am running now")
#
#
# tt = Turtle()
#
# if __name__ == '__main__':
#     tt.climb()
#     tt.run()

print('..... please input a number which I guess')
temp = input('please input:')
guess = int(temp)

if guess == 8:
    print('your guess is right!')

else:
    print('your guess is wrong')

print('game over!!!')
