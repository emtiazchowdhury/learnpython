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
'''


def print_until_divisible_by_5():
    for number in range(1, 21):  # Loop from 1 to 20
        if number % 5 == 0:
            print(f"Number divisible by 5 found: {number}")
            break  # Exit the loop once a number divisible by 5 is encountered


# Example usage
print_until_divisible_by_5()
