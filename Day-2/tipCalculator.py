#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
no_of_people = input("How many people to split the bill? ")


total_amount = float(bill) + (int(tip)/100) * float(bill)
split = total_amount / int(no_of_people)
payable_amount = round(split, 2)
# payable_amount = "{:.2f}".format(split) # this will make sure that there will be exactly 2 decimal precision in every cases

print(f"Each person should pay: ${payable_amount}")