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
#10
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

#11
credit_score = int(input("Enter your credit score: "))

if credit_score >= 700:
    yearly_income = int(input("Enter your yearly income: "))
    if yearly_income >= 50000:
        print("You can get loan")
    else:
        print("No loan - low income")
else:
    print("No loan - poor credit")

#12
weight = float(input("Enter the weight of the package in kg: "))
express_delivery = input("Is it express delivery? yes/no:  ").strip().lower()

if weight <= 10:
    if express_delivery == 'yes':
        print("Your shipping cost if $10")
    else:
        print("Your shipping cost if $5")
else:
    if express_delivery == 'yes':
        print("Your shipping cost if $30")
    else:
        print("Your shipping cost if $15")

#13
gpa = float(input("Enter your gpa: "))
if gpa >= 3.5:
    extra = input("you do extracurr ctivities? yes/no:  ").strip().lower()
    if extra == 'yes':
        print("you can get scolarship")
    else:
        print("no extra - no scolarship")
else:
    print("Lowe gpa - no scolarship")

#14
number = int(input("Enter a number: "))
result = 'Even' if number % 2 == 0 else 'Odd'
print(f"the number {number} is {result}")

age=int(input("Enter your age: "))
status="Adult" if age >= 18 else "Minor"
print(f"You are an {status}")

def process_list(list):
    match list:
        case []:
            print("The list is empty")
        case [a, b]:
            print(f"The has {a} and {b}")
        case [a, b, c, d]:
            print(f"The has {a} and {b} and {c} and {d}")
        case []:
            print(f"list has more than specified items")


process_list([5, 5])


#15
def process_dic(d):
    match d:
        case {"name": name, "age": age}:
            print(f"my name is {name}and I am {age} years old")
        case {"name": name}:
            print(f"my name is{name}")
        case {"age": age}:
            print(f"my age is {age}")
        case _:
            print(f"unknown form dictionary")


process_dic({"name":"james","age": 29})
process_dic({"name":"james"})
process_dic({"age": 29})
process_dic({"location":"New York"})

#16
def process_structure(structure):
    match structure:
        case {"data": {"numbers": [a, b, c], "info": {"name": name}}}:
            print(f"my Name is {name} and numbers: {a}, {b}, {c}")
        case {"data": {"numbers": [a, b], "info": {"name": name}}}:
            print(f"my Name is {name} and numbers: {a}, {b}")
        case _:
            print(f"unknown form dictionary")


process_structure({"data": {"numbers": [1, 2, 3], "info": {"name": "Alice"}}})
process_structure({"data": {"numbers": [1, 2], "info": {"name": "Alice"}}})
process_structure({"data": {"numbers": [1, 2]}})

#17
def can_attend_event(weekend, holiday, special_invitation):
    if weekend or holiday or special_invitation:
        return "You can attend events"
    else:
        return "You can not attend events"
print(can_attend_event(True, True, True))
print(can_attend_event(True, True, False))
print(can_attend_event(True, False, False))
print(can_attend_event(False, False, False))

def check_number_in_range_and_divisibility(number, start, end, divisor):
    if start <= number <= end and number % divisor != 0:
        return f"{number} within the range and is not divisible by {divisor}"
    else:
        return f"{number} does not meet the condition"


print(check_number_in_range_and_divisibility(50, 5, 8, 9))
print(check_number_in_range_and_divisibility(10, 2, 5, 2))

def access_premium_content(subscription, current_promotion):
    if subscription == 'Premium' or current_promotion:
        return "Access granted to Premium content"
    else:
        return "Access Denied to Premium content"


print(access_premium_content("Premium", False))
print(access_premium_content("Basic", True))
print(access_premium_content("Basic", False))

#
def categorize_number(number):
    match number:
        case _ if number <10:
            return("Low")
        case _ if 10 <= number <= 50:
            return("Medium")
        case _ if number > 50:
            return("High")


print(categorize_number(5))
print(categorize_number(45))
print(categorize_number(55))

def process_string(s):
    match s:
        case s if s.isdigit():
            return "String is numeric"
        case s if s.isalpha():
            return "String is alphabtic"
        case s if s.isalnum():
            return "String is alpha numeric"
        case s if len(s) > 10:
            return "String is too long"
        case _:
            return "String does not match any special case"

print(process_string("123"))
print(process_string("Hello"))
print(process_string("Thisislong sdfsfsdf sdfsdfsdfewf sdgwrgsdfvs rgwergsdf srwrtwsfsdf ssfsdf"))
print(process_string("Hello123"))
#
def determine_role(role):
    match role:
        case "admin" | "Admin":
            return "Role: Admin"
        case "editor" | "Editor":
            return "Role: Editor"
        case "viewer" | "Viewer":
            return "Role: Viewer"
        case _:
            return "Role not recognized"

print(determine_role("Admin"))
print(determine_role("Editor"))
print(determine_role("Viewer"))
print(determine_role("Guest"))
'''