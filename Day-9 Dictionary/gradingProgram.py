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
    score = student_socre[student]
    if score > 90 :
        student_grades[student] = "Outstanding"
    elif score > 80 :
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 :
        student_grades[student] = "Acceptable"
    else :
        student_grades[student] = "Fail"

print(student_grades)