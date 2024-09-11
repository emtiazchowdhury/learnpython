
# To do Small Problem: Find out the start_date value of DevOps course for Alice from student_info dictionary, your code should also ensure there is DevOps Course.
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
    print(student.keys())
    print(student.values())
# To do Small Problem: Find out the start_date value of DevOps course for Alice from student_info dictionary, your code should also ensure there is DevOps Course.