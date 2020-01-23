# TASK 1
# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No". 
# Hint: Use input () to get the persons input


user_input = input('enter your message: ')

if user_input.upper() == 'YES':
    print('yes') 
else:
    print('No')

# TASK2

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

# TASK3

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

# TASK 4
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

# TASK 5

# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
#  write a program to print the first half values in one line and
#  the last half values in one line.
#  sample output => 12345
#                  678910

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


# MILESTONE TASK 
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary
#  by getting the inputs basic salary and benefits. Create 5 different class methods which will
#  calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, grossSalary and netSalary. 
# NB: Use KRA, NHIF and NSSF values provided in the link below.
# https://www.aren.co.ke/payroll/taxrates.htm  
# https://calculator.co.ke/kra-salary-income-tax-paye-calculator



# Task 6
task_list = [23, 'Jane', ['Lesson 23', 560, {'currency' : 'KES'}], 987, (76,'John')]
# Determing type of variable in task_list using an inbuilt function

check_type = type(task_list)
print(task_list)

# Print KES

print(task_list[2][2]['currency'])

# Print 560

print(task_list[2][1])


# Use a function to determine the length of taksList

length_task_list = len(task_list)
print(length_task_list)

# Change 987 to 789 without using an inbuilt -method or Assignment

# FIRST WAY
task_list[3] = 789
print(task_list)

# SECOND WAY
x = task_list[3]
y = str(x)
z = y[::-1]
task_list.insert(3, z)

# Change the name “John” to “Jane” .

task_list[4] = (76, 'Jane')
print(task_list)

# Task 7
# Check for password length using if else conditional statements
# if less than 5 print too short
# if greater than 15 print too many characters
# if in between print login successful

password = input('Enter your Password: ')

if len(password) < 5:
    print('Password too short')
elif len(password) > 15:
    print('Too many characters')
else:
    print('Login Successful')

# TASK8
#GRADING SYSTEM
# create a GRADING SYSTEM
# ask for students marks in five subjects
# calculate the average and grade them ABCD depending on their performance

mathematics = int(input('Enter your mathematics results: '))

if mathematics > 100 or mathematics < 0:
    print('please enter valid marks')

Science = int(input('Enter your science results: '))

if Science > 100 or Science < 0:
    print('please enter valid marks')

Kiswahili = int(input('Enter your kiswahili results: '))

if Kiswahili > 100 or Kiswahili < 0:
    print('please enter valid marks')

Social_studies = int(input('Enter your socialstudies results: '))

if Social_studies > 100 or Social_studies < 0:
    print('please enter valid marks')

English = int(input('Enter your English results: '))

if English > 100 or English < 0:
    print('please enter valid marks')


total_marks = mathematics + Science + Kiswahili + Social_studies + English

# print(total_marks)


average = total_marks / 5 

if average <= 100 and average >= 80 :
    print(f'your average is {average} your grade is  A')
elif average < 80 and average >=70 :
    print(f' your average is {average} your grade is B')
elif average < 70 and average >= 60  :
    print(f'your average is {average} your grade is C')
elif average < 50 and average > 0:
    print('Enter valid mathematics marks')
else:
    print('Enter valid marks')

# TASK 9
# login to facebook
# enter your username
# if true enter your email if true enter password
# if invald respond 

print('WELCOME TO FACEBOOK LOGIN PAGE')

username = 'Mark'
email = 'mark@gmail.com'
password = 123456


inputted_username = input('Enter your Username: ')

if inputted_username.capitalize() == username:
    user_email = input('now Enter your Email: ')
    if user_email == email:
        user_password = int(input('Enter your Password: '))
        if user_password == password:
            print('Welcome to Facebook')
        else:
            print('invalid password')
    else:
        print('the email you enter does not exist')
else:
    print('please enter a valid username')

# TASK 10
# BUY AIRTIME APPLICATION
account_balance = 50

airtime = int(input('Enter amount to spend: '))

new_balance = account_balance - airtime

if account_balance > airtime:
    print(f'you have received {airtime} mbs new balance is {new_balance}')
else:
    print(f'you have insufficient funds your balance is {account_balance}')

# TASK 11
#two numbers = print the greatest

number_one = int(input('Enter a number to compare: '))

number_two = int(input('Enter number to compare with: '))

if number_one > number_two:
    print(f'{number_one} is greater then {number_two}')
else:
    print(f'{number_two} is greater then {number_one}')


# TASK 12
# 2.A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classes_held = int(input('Enter number of classes held: '))
classes_attended = int(input('Enter number of classes attended: '))


attendance_percentage = int((classes_attended/classes_held) * 100)



if attendance_percentage > 100:
    print('classes attended cannot exceed classes held')
elif attendance_percentage > 75:
    print(f'your attendance is {attendance_percentage}%')
    print('Proceed to the examination')
else:
    has_medical_cause = input('Do you have a medical cause respond with Y/N: ')
    if has_medical_cause.lower() == 'y':
        print('Proceed to the examination')
    else:
        print('Not allowed for the test')
    

# 3.Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.


# TASK 13
# 4.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.


quantity = int(input('Enter purchased quantity: '))

total_cost = quantity * 10

if total_cost > 1000:
    new_total = total_cost * 0.9
    print(f'your total cost is {new_total}')
else:
    print(f'your total cost is {total_cost}')

# TASK 14
#  Accept two int values from the user and return their product. 
# If the product is greater than 1000, then return their sum

int_one = int(input('Enter a number: '))
int_two = int(input('Enter a second number: '))

product = int_one * int_two

if product > 1000:
    print(int_one + int_two)
else:
    print(product)

# TASK 15
# Write a Python program to check if all dictionaries in a list are empty or not.

# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


# TASK 16
# Write a program that prints the numbers 1-100, each on a new line
# For each number that is a multiple of 3, print “Fizz” instead of the number
# For each number that is a multiple of 5, print “Buzz” instead of the number
# For each number that is a multiple of both 3 and 5, print “FizzBuzz” instead of the number
# if doesnt fall in any category print the number
# Now that you know what you need to write, you can get started!

def fizz_buzz(number):
    for num in range(number + 1):
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else:
            print(num)

# TASK 17
# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C or D
# tell them to go to room CD
# If their first name starts with another letter,
#  ask for their last name
# IF their last name starts with Z, 
# tell them to go to room Z
# if their last name starts with any other letter,
# tell them to go to room OTHER

#######################
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

first_name = input('Enter your first name: ')

if first_name[0].upper() in ('A', 'B'):
    print('Go to room AB')
elif first_name[0].upper() in ('C', 'D'):
    print('Go to room CD')
else:
    last_name = input('Enter your last name: ')
    if last_name[0].upper() == 'Z':
        print('GO TO ROOM Z')
    else:
        print('GO TO ROOM OTHER')

# TASK 18
# use for loop to print odd or even alongside each number 
nums = [1,2,3,4,5,6,7,8,9,]

for num in  nums:
    if num % 2 == 0:
        print(num, 'Is even')
    else:
        print(num, 'Is odd')

# TASK 19
# # print 1-10 using while loop 

i = 1

while i <= 10 :
    print(i)
    i += 1

# 10 to 1

a = 10

while a >= 0:
    print(a)
    a -= 1



# TASK 20
# source = https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included).

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

# A SECOND WAY
multiples = []

for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        multiples.append(str(number))

print(','.join(multiples))


# TASK 21
# 3. Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears
#  again until the guess is correct, on successful guess,
#  user will get a "Well guessed!" message, and the program will exit.

import random

number = random.randint(1,9)
print(number)

guess_count = 0

while guess_count <= 9 :
    guess = int(input('Guess a number between 1 and 9: '))
    if guess == number:
        print('Congratulations you guessed right')
        break
    guess_count +=1

