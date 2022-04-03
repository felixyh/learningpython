# Design the game, guess a number, try maximum 3 times
import random

print("This is the game program")

secret = random.randint(1, 10)
temp = input("please input a number:")
guess = int(temp)

count = 3

while count > 1 and guess != secret:
    if guess > secret:
        print("your guess number is big, input a smaller one")
    else:
        print("your input number is small, input a bigger one")
    temp = input("please input a number:")
    guess = int(temp)
    count = count - 1

if guess == secret:
    print('your guess is exactly right!! Congrats!')
else:
    print('You already tried three times, game over!')


