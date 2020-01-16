# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No". 
# Hint: Use input () to get the persons input


user_input = input('enter your message: ')

if user_input.upper() == 'YES':
    print('yes') 
else:
    print('No')


# Implement a function that takes as input three variables, and returns the largest of the three. Do this 
# without using the Python max () function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us. 

def maximum_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b 
    else:
        return c

result = maximum_of_three(15,66,7)
print(result)


# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes
#  a new list of only the first and last
#  elements of the given list. For practice, write this code inside a function

# FIRST WAY
a = [5, 10, 15, 20, 25]

b = []

b.append(a[0])
b.append(a[-1])
print(b)

# SECOND WAY

my_list = [5, 10, 15, 20, 25]

new_list = my_list[::4]

print(new_list)


# Ask the user for a number. Depending on whether the number is even or odd,
#  print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

user_number = int(input('Enter a Number: '))

if user_number % 2 == 0:
    print(f'{user_number} is Even')
else:
    print(f'{user_number} is Odd')

    
# If the number is a multiple of 4, print out a different message.


user_number = int(input('Enter a Number: '))

if user_number % 4 == 0:
    print(f'{user_number} is a multiple of four')
elif user_number % 2 == 0:
    print(f'{user_number} is Even')
else:
    print(f'{user_number} is Odd')

# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
#  write a program to print the first half values in one line and
#  the last half values in one line.

# ONE WAY

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

first_half = my_tuple[:5]
last_half = my_tuple[5:]

first_half_to_string = str(first_half).strip('()')
last_half_to_string = str(last_half).strip('()')


print(first_half_to_string)
print(last_half_to_string)

# SECOND WAY
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = str(a[:5])
c = str(a[5:])

d = b.replace('(', '')
e = d.replace(')', '')

print(e)

f = c.replace('(', '')
g = f.replace(')', '')

print(g)



