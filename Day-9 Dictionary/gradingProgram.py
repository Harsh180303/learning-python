student_socre = {
    "Harsh": 99,
    "Rajkumar": 100,
    "Darshit": 79,
    "Aditi": 44,
    "Sarthak": 84,
    "Vikas": 85,
}

student_grades = {}

for student in student_socre:
    if student_socre[student] >= 91 and student_socre[student] <= 100 :
        student_grades[student] = "Outstanding"
    elif student_socre[student] >= 81 and student_socre[student] <= 90 :
        student_grades[student] = "Exceeds Expectations"
    elif student_socre[student] >= 71 and student_socre[student] <= 80 :
        student_grades[student] = "Acceptable"
    else :
        student_grades[student] = "Fail"

print(student_grades)