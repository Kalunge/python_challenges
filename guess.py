# GUESSING GAME USING WHILE LOOP

import random

random_number = random.randint(1, 20)
print(random_number)


guess_count = 1

while guess_count <= 5 :
    guess = int(input('Enter a number: ')) 
    if guess != random_number:
        if ( random_number - guess) > 3:
            print('WRONG PLEASE TRY AGAIN YOU ARE FAR FROM THE NUMBER ')
        elif (random_number - guess) <= 3:
            print('WRONG PLEASE TRY AGAIN YOU ARE ALMOST THERE ')
        guess_count += 1
        remaining_attempts = 6 - guess_count
        print(f'{remaining_attempts} Attempts remaining!! ')
    else:
        print('HURRAYYYY YOU WON !! ')
        break