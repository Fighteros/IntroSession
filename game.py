

from random import randint


x = randint(1, 20)

while True:
    y = int(input('the number is ?: '))
    if(y == x):
        print('you win!')
        break
    elif(y > x) :
        print('the number you entered is large')
    elif (y < x):
        print('the number you entered is small')

