# Task 1: Temperature Conversion
'''
c = int(input("Enter the temperature in Celsius: "))

def changingTypeOfTemperature(temp):
    print ("Temperature in F: ",((9/5)* temp)+32)

changingTypeOfTemperature(c)
'''
# Task 2: Basic Calculator
'''a = int(input("enter a number: "))
b = int(input("enter another number: "))
d = input("What do you want? +, -, *, / ")

if d == "+":
    print(a+b)
elif d == "-":
    print(a-b)
elif d == "*":
    print(a*b)
elif d == "/":
    print(a/b)
'''
#Task 3: Even/Odd Check
'''
a = int(input("enter a number: "))

def indenteficationEvenOrOdd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

indenteficationEvenOrOdd(a)
'''

# Task 4: Basic level
'''
health = int(input("enter a number: "))
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True
'''
# Task 5: Birthday
'''
number_of_month = int(input("Enter the number of the month: "))
def season_events(number_of_month):
    name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    words = {"winter":"White snow fell outside the window","spring":"Birds sang beautiful songs", "summer":"The sun shone brighter than ever", "autumn":"The harvest was incredible"}

    if number_of_month <1 or number_of_month >12:
        print("You need to enter the real number of the month")
    current_month = name[number_of_month - 1]

    if number_of_month in [12, 1, 2]:
        print(f"You were born in {current_month}. {words['winter']}")
    elif number_of_month in [3, 4, 5]:
        print(f"You were born in {current_month}. {words['spring']}")
    elif number_of_month in [6, 7, 8]:
        print(f"You were born in {current_month}. {words['summer']}")
    elif number_of_month in [9, 10, 11]:
        print(f"You were born in {current_month}. {words['autumn']}")

season_events(number_of_month)
'''