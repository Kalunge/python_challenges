# SIM CARD
print('WELCOME TO SAFARICOM. KINDLY UNLOCK YOUR SIMCARD TO PROCEED')
attempts = 2
pin = 4040

while attempts < 3:
    entered_pin = int(input(f'Enter you sim pin. you have {attempts} remaining: '))
    if entered_pin != pin:
        attempts += 1
        remaining_attempts = 3 - attempts 
        print(f'Wrong pin you have {remaining_attempts} attempts remaining')
        if remaining_attempts == 0:
            print('SIMCARD BLOCKED')
    else:
        print('WELCOME TO THE BETTER OPTION')
        break
