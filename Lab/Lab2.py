'''
#1
number=int(input("Enter a number: "))
if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is 0")

#2
temperature=float(input("Enter the temperature in degrees celsius: "))

if temperature<=0:
    print("Its freezing")
elif 0<temperature<=10:
    print("Its cold")
elif 10<temperature<=25:
    print("Its mild")
else:
    print("Its Hot")

#3
age=int(input("Input your age: "))
if age <18:
    print(f"since you are {age} you are not allowed to vote")
else:
    print(f"since you are {age} you are allowed to vote")

#4
temperature=float(input("What is the temperature outside: "))
raining=input("Its raining yes/no: ").strip().lower() == 'yes'
snowing=input("Its snowing yes/no: ").strip().lower() == 'yes'
if temperature>80 and not raining and not snowing:
    print("You can go outside")
else:
    print("Stay indoor")

#5
score=int(input("What is your score? "))
teacher_recommendation=input("Teacher has recommendation yes/no: ").strip().lower() == 'yes'
if score >= 50 or teacher_recommendation:
    print("You passed")
else:
    print("You failed")

#6
is_member=input("Are you a member yes/no: ").strip().lower() == 'yes'
has_coupon=input("Do you have a coupon yes/no: ").strip().lower() == 'yes'

if is_member or has_coupon:
    print("You can get discount")
else:
    print("You can not get discount")

#7
logged_in=input("are you logged in yes/no: ").strip().lower() == 'yes'
premium_package=input("do you have premium package yes/no: ").strip().lower() == 'yes'
if logged_in and premium_package:
    print("Access Granted")
else:
    print("Access Denied")

#8
vacation=input("are you vacation yes/no: ").strip().lower() == 'yes'
weekend=input("is it weekend yes/no: ").strip().lower() == 'yes'
if vacation or weekend:
    print("Vacation Time")
else:
    print("Not vacation time")

#8
role=input("are you admin/user: ").strip().lower()
is_member=input("are you member yes/no: ").strip().lower() == 'yes'
if role == 'admin' or is_member:
    print("Access Granted")
else:
    print("Access Denied")

number = float(input("Enter the number: "))
def my_function(number):
    if number > 0:
        for i in range(3, 16, 2):
            print(i)
        else:
            print("Number out of range")
my_function(number)
#9
def day_of_the_week(day):
    match day:
        case "Saturday" | "Sunday":
            print("Its weekend")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("Its a weekday")


day_of_the_week("Monday")

def categorize_number(number):
    match number:
        case number if number > 0:
            print(f"You entered {number}. Its a positive number.")
        case number if number < 0:
            print(f"You entered {number}. Its a negative number.")
        case number if number == 0:
            print(f"You entered {number}. The number is 0")


categorize_number(10)
categorize_number(-10)
categorize_number(0)

def type_of_input(input):
    match input:
        case str():
            print("Its a string")
        case list():
            print("Its a list")
        case dict():
            print("Its a dict")
        case _:
            print("Its unknown type")

type_of_input("Hello")
type_of_input([1,2])
type_of_input({"Key":"value"})
type_of_input(5)
'''