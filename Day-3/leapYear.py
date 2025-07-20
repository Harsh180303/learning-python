# 🔁 Leap Year Rules :---
# Divisible by 4 → Leap year
# Except if it's divisible by 100 → Not a leap year
# Unless it’s divisible by 400 → Leap year again

year = int(input("Whick year do you want to check?"))

if year % 400 == 0 :
    print("leap year")
elif year % 100 == 0 :
    print("not a leap year")
elif (year % 4 == 0) :
    print("leap year")
else :
    print("not a leap year")