# TASK 2
# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# temp = input('Enter temperatures you wish to convert eg 20C or 5F: ')

# degrees = int(temp[:-1])
# convention = temp[-1]
# # print(degrees)
# # print(convention)

# if convention.upper() == 'C':
#     result = int((5/9) * (degrees -32))
#     print(f'{degrees} celcius is {result} fareinheit')

# elif convention.upper() == 'F':
#     result = 

    


# C = (5/9) * (F - 32)












    
# TASK 4
# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

mylist = [1,2,3,4,5,4,3,2,1]

for item in mylist:
    print(item * ' *')


n = 5
for a in range(n):
    print(a)

for i in range(n):
    for j in range(i):
        print('*', end='')
    print('')
# TASK 5
# 5. Write a Python program that accepts a word from the user and reverse it.

# # TASK 6
#  Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

