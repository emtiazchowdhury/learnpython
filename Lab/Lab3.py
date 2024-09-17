#1
'''
def print_even_numbers():
    number=2
    while number<=30:
        print(number)
        number +=2

print_even_numbers()

def test():
    number=10
    while number > 0:
        print(number)
        number -=1

test()

def sum_numbers():
    total = 0
    number = 1
    while number <= 100:
        total += number
        number += 1
        print("Total sum: ", total)


sum_numbers()

def print_characters(s):
    for char in s:
        print(char)


print_characters("Hello")

def print_hello(names):
    for name in names:
        print(f"hello my name is {name}")


print_hello(['James','Rob','Tom'])

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print("Factorial: ", result)


factorial(5)

def print_numbers():
    for number in range(5,15):
        print(number)

print_numbers()

def print_square():
    for number in range(1, 15):
        print(number ** 2)


print_square()

fruits = ["apples","banana","orange"]

for fruit in fruits:
    print(fruit)



def generate_even_numbers():
    even_numbers = [number for number in range(0, 21, 2)]
    print(even_numbers)


generate_even_numbers()

def print_non_divisible_by_3():
    for number in range(1, 16):  # Loop from 1 to 15
        if number % 3 == 0:
            continue  # Skip numbers divisible by 3
        print(number)

# Example usage
print_non_divisible_by_3()


def print_numbers_greater_than_5(numbers):
    for number in numbers:
        if number <= 5:
            continue
        print(number)


print_numbers_greater_than_5([1, 3, 5, 7, 9, 11])


def print_numbers_excluding_7():
    for number in range(1, 11):  # Loop from 1 to 10
        if number == 7:
            continue  # Skip the number 7
        print(number)

# Example usage
print_numbers_excluding_7()

def skip_numbers_7(numbers):
    for number in numbers:  # Loop from 1 to 10
        if number > 50:
            break
        print(number)


# Example usage
skip_numbers_7([10, 11, 85, 41, 22, 1, 15, 45, 25])

def ask_until_stop():
    while True:
        user_input = input("Enter something (type 'stop' to exit): ")
        if user_input.lower() == 'stop':
            break


ask_until_stop()

def print_until_divisible_by_5():
    for number in range(1, 21):  # Loop from 1 to 20
        if number % 5 == 0:
            print(f"Number divisible by 5 found: {number}")
            break  # Exit the loop once a number divisible by 5 is encountered


# Example usage
print_until_divisible_by_5()


import json

# Python object (dictionary)
employee = {"name": "John Doe", "age": 30, "department": "Engineering"}

# Serialization
employee_json = json.dumps(employee, indent=4)
print("Serialized JSON:", employee_json)

# Deserialization
employee_dict = json.loads(employee_json)
print("Deserialized Dictionary:", employee_dict)

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number == 3:
        continue
    print(number)
print("========")
for number in numbers:
    if number == 5:
        break
    print(number)

fruits=["apple", "Orange", "Pear"]

for fruit in fruits:
    if fruit == 'Orange':
        continue
    print(fruit)

number = [1, 2, 3]
for i in range(len(number)):
    number[i] *= 2
print(number)

profile = {"Alice": 25, "Bob": 30, "Charlie": 35}

# print(ages.keys())
# print(ages.values())

for name,age in profile.items():
    print(f"Hello my name is {name} and I am {age}")

profile = {"name": "Alice", "age": None, "email": 35}

for key,value in profile.items():
    if value is None:
        if value is None:
            print(f"{key} is missing.")
    else:
        print(f"{key}: {value}")



def fruits_upper_case(fruits):
    for fruit in fruits:
        print(fruit.capitalize())


fruits_upper_case(['apple', 'banana', 'cherry'])



def add_numbers(numbers):
    total_sum = 0
    for i in numbers:
        total_sum += (i)
        print(total_sum)


add_numbers([1, 3, 6, 44])

def filter_odd_number(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers


oddnum=filter_odd_number([1, 5, 88, 4, 6, 4, 7])
print(oddnum)

def print_student_keys(student_grades):
    for key in student_grades:
        print(key)  # Print each key in the dictionary

# Example usage
print_student_keys({'Alice': 85, 'Bob': 90, 'Charlie': 78})


def print_student_keys(student_grades):
    for key, value in student_grades.items():
        print(f"hellow my name is {key} and I am {value} years old")  # Print each key in the dictionary

# Example usage
print_student_keys({'Alice': 85, 'Bob': 90, 'Charlie': 78})

def average_of_values(data):
    total_sum = 0
    count = 0
    for value in data.values():
        total_sum += value  # Sum all the values
        count += 1
    if count > 0:
        average = total_sum / count
        print(f"Average value: {average}")
    else:
        print("No values to average")

# Example usage
average_of_values({'Alice': 85, 'Bob': 90, 'Charlie': 78})



def replace_none_with_unknown(data_list):
    modified_list = ['Unknown' if item is None else item for item in data_list]
    print(modified_list)


# Example usage
replace_none_with_unknown(['Alice', None, 'Bob', None, 'Charlie'])


def filter_none_values(data_list):
    filtered_list = [item for item in data_list if item is not None]
    print(filtered_list)

# Example usage
filter_none_values(['Alice', None, 'Bob', None, 'Charlie'])
'''


def check_none(dict):
    for key, value in dict.items():
        if value is None:
            print(f"{value}")


check_none({"name": "Alice", "Age": None})
