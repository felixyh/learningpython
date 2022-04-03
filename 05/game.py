# Design the game, guess a number, try maximum 3 times
import random

print("This is the game program")

secret = random.randint(1, 10)

guess = 0
count = 3


while count > 0 and guess != secret:

    temp = input("please input a number:")
    while not temp.isdigit():
        print('your input is not a number, please input again')
        temp = input("please input a number:")
    guess = int(temp)
    if guess > secret:
        print("your guess number is big, input a smaller one")
    else:
        print("your input number is small, input a bigger one")

    count = count - 1

if guess == secret:
    print('your guess is exactly right!! Congrats!')
else:
    print('You already tried three times, game over!')

