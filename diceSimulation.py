import random

diceNumber = 0
user_input = 'y'


def throw_dice():
    i = random.randint(0, 6)
    print("Dice:: " + str(i + 1))


while user_input == 'y':
    throw_dice()
    user_input= input("Do you want to throw again (y/n) ? ")
    while user_input != 'y' and user_input != 'n':
        print('Enter a valid input.')
        user_input = input("Do you want to throw again (y/n) ? ")


print("\nThank you for playing.\nHave a great day!")