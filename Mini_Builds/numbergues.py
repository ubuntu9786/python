import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("guess an number: "))
        if guess < random_number:
            print('too low')
        elif guess > random_number:
            print('too hight')

    print('noice')
guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high or too low: ').lower
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'we guessed your number {guess}')

computer_guess(10)


