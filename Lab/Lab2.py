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
'''