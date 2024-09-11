#Print in Python
print('hello world!')

#Data Type in Python [Python understands data type automatically based on the data. There is no need to declare it explicitly.]
age = 25  #Integer.
pi = 3.5  # Float.
name = 'emtiaz'  #String [single/double quote both acceptable]
is_active = True  #Boolean [True/false not true/false]

#List: mutable/can be changed [ we can can access, add and remove]
fruits = ['apple', 'orange', 'pear']
print(fruits)
#Add Items to List: use append() [adds an item to the end of a list]
#fruits = fruits.append('lemmon')
fruits = ['apple', 'orange', 'pear','lemmon']
print(fruits)
#Insert Items to the List: use insert() [inserts and item in a specified position in the list]
fruits.insert(0, 'mango')
print(fruits)
#Remove Item
fruits.remove('mango')
print(fruits)

#Tuple: Its an immutable object can’t be changed after it is created
coordinates = (10, 20)
print(coordinates)


#Dictionary: key Value pair
student = {"name": "Alice", "age": 25}
print(student["name"])
info = {"name": "James", "number":1}
print(info['number'])
student_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": True,
    "courses": [
        {"course_name": "DevOps",
         "start_date": "05/15/2024"
         },
        {"course_name": "DataAnalytics",
         "start_date": "01/15/2025"
         }
    ]
}
for student in student_info["courses"]:
    print(student)
    print(student.keys())
    print(student.values())
# To do Small Problem: Find out the start_date value of DevOps course for Alice from student_info dictionary, your code should also ensure there is DevOps Course.


name = 'Jahidul'
print(name)
name = name.join(" Islam")
print(name)
