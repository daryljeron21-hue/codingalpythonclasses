student_marks = {
    "student_1":{"name":"Reno","marks":85},
    "student_2":{"name":"Jefrin","marks":67},
    "student_3":{"name":"Alen","marks":45},
    "student_4":{"name":"Jeron","marks":95},
    "student_5":{"name":"Seth","marks":70},
    "student_6":{"name":"Abijith","marks":99.9},
    "student_7":{"name":"Sharuk","marks":20},
    "student_8":{"name":"Rohit","marks":35},
    "student_9":{"name":"Rithik","marks":1},
    "student_10":{"name":"Francis VP","marks":0}
}

pass_mark = 40

average_marks_of_class = sum(student["marks"] for student in student_marks.values()) / len(student_marks)
print("Average Marks:", average_marks_of_class)

topper = max(student_marks.values(), key=lambda x: x["marks"])
print("Topper:", topper["name"], "with marks:", topper["marks"])

passed_students = [student["name"] for student in student_marks.values() if student["marks"] >= pass_mark]
print("Students who passed:", ", ".join(passed_students))

failed_students = [student["name"] for student in student_marks.values() if student["marks"] < pass_mark]
print("Students who failed:", ", ".join(failed_students))

lowest_marks_student = min(student_marks.values(), key=lambda x: x["marks"])
print("Student with lowest marks:", lowest_marks_student["name"], "with marks:", lowest_marks_student["marks"])