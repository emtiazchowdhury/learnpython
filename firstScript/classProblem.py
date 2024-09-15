from datetime import datetime

student_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": True,
    "courses": [
        {"course_name": "DevOps",
         "start_date": "1234"
         },
        {"course_name": "DataAnalytics",
         "start_date": "12345"
         }
    ]
}

student_info = student_info["courses"]
student_info = student_info[0]["course_name"]
print(student_info)
#student_info = student_info[]["start_date"]
print(student_info)
# if student_info == "DevOps":
#     student_info = student_info[0]["course_name"]
#     print(student_info)