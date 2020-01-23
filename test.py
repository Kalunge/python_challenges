# SIM CARD
print('WELCOME TO SAFARICOM. KINDLY UNLOCK YOUR SIMCARD TO PROCEED')
attempts = 1
pin = 4040

while attempts <= 3:
    entered_pin = int(input(f'Enter you sim pin. '))
    if entered_pin != pin:
        remaining_attempts = 3 - attempts 
        attempts += 1
        print(f'Wrong pin you have {remaining_attempts} attempts remaining')
        if remaining_attempts == 0:
            print('SIMCARD BLOCKED')
    else:
        print('WELCOME TO THE BETTER OPTION')
        break
