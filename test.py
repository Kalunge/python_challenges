
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

has_medical_cause = input('Do you have a medical cause respond with Y/N: ')

print(f'your attendance is {attendance_percentage}%')

if attendance_percentage > 75 or has_medical_cause.upper() == 'Y':
    print('Proceed to the examination')
elif attendance_percentage > 100:
    print('c')
else:
    print('Not allowed for the test')
    



# 3.Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.



# 4.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

