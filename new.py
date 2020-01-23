# TASK 1

# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No". 
# Hint: Use input () to get the persons input

# TASK2
# Implement a function that takes as input three variables,
#  and returns the largest of the three. Do this 
# without using the Python max () function!
# The goal of this exercise is to think about some internals that
#  Python normally takes care of for us. 


# TASK3

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes
#  a new list of only the first and last
#  elements of the given list. For practice, write this code inside a function


# TASK 4
# Ask the user for a number. Depending on whether the number is even or odd,
#  print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# If the number is a multiple of 4, print out a different message.


# TASK 5

# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
#  write a program to print the first half values in one line and
#  the last half values in one line.
# sample output => 12345
#                  678910



# MILESTONE TASK 
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary
#  by getting the inputs basic salary and benefits. Create 5 different class methods which will
#  calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, grossSalary and netSalary. 
# NB: Use KRA, NHIF and NSSF values provided in the link below.
# https://www.aren.co.ke/payroll/taxrates.htm  
# https://calculator.co.ke/kra-salary-income-tax-paye-calculator



# Task 6
# LIST METHODS
task_list = [23, 'Jane', ['Lesson 23', 560, {'currency' : 'KES'}], 987, (76,'John')]
# Determing type of variable in task_list using an inbuilt function


# Task 6a
# Print KES


# Task 6b
# Print 560


# Task 6c
# Use a function to determine the length of taksList

# Task 6d
# Change 987 to 789 without using an inbuilt -method or Assignment


# Task 6e
# Change the name “John” to “Jane” .


# Task 7
# Check for password length using if else conditional statements
# if less than 5 print too short
# if greater than 15 print too many characters
# if in between print login successful



# TASK8
# create a GRADING SYSTEM
# ask for students marks in five subjects
# calculate the average and grade them ABCD depending on their performance


# TASK9
# create a page to login to facebook
# have three variables for username, email and pasword
# let the user enter their username
# if true enter ask for their email email if true ask for their  password
# if invald respond 
# if any detail is wrong notify the user. proceed only if details are correct


# TASK 10
# BUY AIRTIME APPLICATION
# have users balance
# let them buy airtime if balance is okay
# ask them for the amount they want to spend and display their balance after transaction


# TASK 11
#ask for two numbers and print the greatest



# Task 12
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.


# TASK12 b
# 3.Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

# TASK 13
# 4.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.


# TASK 14
# Accept two int values from the user and return their product. 
# If the product is greater than 1000, then return their sum


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
# name = input('What is your name:  ')



# TASK 17
# Abigail and Benson are playing Rock, Paper, Scissors.

# Each game is represented by an array of length 2, where the first element represents what Abigail played and the second element represents what Benson played.

# Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".

# R stands for Rock
# P stands for Paper
# S stands for Scissors


# EXAMPLE:

# calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]) ➞ "Abigail"

#  Ben wins the first game (Paper beats Rock).
#  Abigail wins the second game (Rock beats Scissors).
#  Abigail wins the third game (Scissors beats Paper). 
#  Abigail wins 2/3.


# calculate_score([["R", "R"], ["S", "S"]]) ➞ "Tie"

# calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) ➞ "Tie"



# # TASK 18
#  Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4


# TASK 19
#  Write a Python program that accepts a word from the user and reverse it.


# TASK20
#  Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5



# TASK21
#  Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34


# TASK 22
# Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz



# TASK 23
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
#  The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


# TASK 24
# Write a Python program that accepts a sequence of lines (blank line to terminate) 
# as input and prints the lines as output (all characters in lower case).


# TASK 25
# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers
#  that are divisible by 5 in a comma separated sequence.

# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010


# TASK 26
# Write a Python program that accepts a string and calculate the number of digits and letters.

# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2


# TASK 27
# Write a Python program to check the validity of password input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


# TASK 28
# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
#  The numbers obtained should be printed in a comma-separated sequence


# TASK 29
# Write a Python program to print alphabet pattern 'A'.
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *

# 29b. 'L'

#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****

# 29c. 'M'

#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *

# 29d. 'o'

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   ***

# 29e. 'P'

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *


# 29f. 'R'

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *


# 29g. the following patterns

#  ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 


 
#  ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo 



#  *****                                                                  
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    * 


#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 


#  *   *                                                                  
#  *   *                                                                  
#   * *                                                                   
#    *                                                                    
#   * *                                                                   
#  *   *                                                                  
#  *   *

# *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******


# TASK 30
#  Write a Python program to calculate a dog's age in dog's years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73


# Task 31
# Write a Python program to check whether an alphabet is a vowel or consonant.
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.


# TASK 32
# Write a Python program to convert month name to a number of days. 
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 

# TASK 33
# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


# TASK 34
#  Write a Python program to check a string represent an integer or not.
# Expected Output:

# Input a string: Python                                                  
# The string is not an integer.  



# TASK 35.
Write a Python program to check a triangle is equilateral, isosceles or scalene.

# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:

# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle  

# TASK 36
#  Write a Python program that reads two integers representing a month and day and prints the season for that month and day
# Expected Output:

# Input the month (e.g. January, February etc.): july                     
# Input the day: 31                                                       
# Season is autumn  



# TASK 37.
# Write a Python program to display astrological sign for given date of birth.
# Expected Output:

# Input birthday: 15                                                      
# Input month of birth (e.g. march, july etc): may                        
# Your Astrological sign is : Taurus 



# TASK 38.
#  Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born. Go to the editor
# Expected Output:

# Input your birth year: 1973                                             
# Your Zodiac sign : Ox  


# TASK 39.
#  Write a Python program to find the median of three values. Go to the editor
# Expected Output:

# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0   

# TASK 40. 
# Write a Python program to get next day of a given date.
# Expected Output:

# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24   

#  TASK 41. 
# Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.


# TASK 42.
#  Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:

# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48                                                              
# 6 x 9 = 54                                                              
# 6 x 10 = 60 

# TASK 43.
#  Write a Python program to construct the following pattern, using a nested loop number.

# Expected Output:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999