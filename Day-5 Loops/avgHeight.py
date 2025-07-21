# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Condition is we can't use len and sum function
# length = len(student_heights)
# addition = sum(student_heights)

# avg = round(addition / length)
# print(avg)

number_of_students = 0
for student in student_heights:
  number_of_students += 1

total_height = 0
for height in student_heights :
  total_height += height

print(total_height/number_of_students)
print(round(total_height/number_of_students))