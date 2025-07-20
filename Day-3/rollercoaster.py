print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if (height >= 120) :
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if (age >= 45 and age <= 55) :
        print("You can enjoy ride for free!")
    elif (age >= 18) :
        print("Adult tickets are $12")
        bill = 12
    elif (age >= 12) :
        print("Youth tickets are $7")
        bill = 7
    else :
        print("Child tickets are $5")
        bill = 5
    
    wants_photo = input("Do you want to take a photo? Y or N. ")
    wants_photo = wants_photo.capitalize()
    # print(wants_photo)
    if wants_photo == "Y" :
        bill += 3
    
    print(f"Your final bill is {bill}")
    
else: 
    print("Sorry, you have to grow taller before you ride.")