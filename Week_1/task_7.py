'''Task 7- Checking for zero (1point)
Add a division by zero check to the previous task.
Write down the verification using the abbreviated form of the condition.'''

number_1 = int(input('Enter a number: '))
operation = input('Enter an operation: ')
number_2 = int(input('Enter a number: '))

if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/' and number_2 != 0:
    print(number_1 / number_2)
else:
    print('Error')
