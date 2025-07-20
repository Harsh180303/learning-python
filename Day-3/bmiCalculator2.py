# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2), 2)

if bmi <= 18.5 :
    category = "underweight"
elif bmi <= 25 :
    category = "normal weight"
elif bmi <= 30 : 
    category = "overweight"
elif bmi <= 35 :
    category = "obese"
else :
    category = "clinically obese"

print(f"Your bmi is {bmi}, you are {category}")