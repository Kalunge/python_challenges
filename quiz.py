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


# MILESTONE TASK 
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary
#  by getting the inputs basic salary and benefits. Create 5 different class methods which will
#  calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, grossSalary and netSalary. 
# NB: Use KRA, NHIF and NSSF values provided in the link below.
# https://www.aren.co.ke/payroll/taxrates.htm  
# https://calculator.co.ke/kra-salary-income-tax-paye-calculator



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
task_list.insert(3, a)

# Change the name “John” to “Jane” .

task_list[4] = (76, 'Jane')
print(task_list)

# Check for password length using if else conditional statements

password = input('Enter your Password: ')

if len(password) < 5:
    print('Password too short')
elif len(password) > 15:
    print('Too many characters')
else:
    print('Login Successful')

#GRADING SYSTEM

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


